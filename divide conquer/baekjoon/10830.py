import sys
sys.setrecursionlimit(10 ** 6)
def input(): return sys.stdin.readline().strip()

# 모듈러 연산 적용


def mul(X, Y):
    # 2차원 배열에서 왼쪽 행, 오른쪽 열(== [Y[k][j] for k in range(n)])의 각 원소 곱셈의 합을 원소로 갖는 2차원 배열을 반환
    return [[sum([x * y for x, y in zip(X[i], [Y[k][j] for k in range(n)])]) % 1000 for j in range(n)] for i in range(n)]


# 1 제곱일 때도 나머지 적용
def f(a, b):
    temp = [[a[i][j] % 1000 for j in range(n)] for i in range(n)]
    if b == 1:
        return temp
    elif b % 2 == 1:
        return mul(temp, f(a, b - 1))
    else:
        part = f(a, b // 2)
        return mul(part, part)


n, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = f(board, b)

for a in answer:
    print(' '.join(map(str, a)))
