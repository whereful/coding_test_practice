
# https://solved.ac/arena/1/editorial

import sys


def input(): return sys.stdin.readline().rstrip()


def main():

    MOD = 10**9 + 7
    N, K = map(int, input().split())
    c = [0]*K
    *A, = map(int, input().split())

    # 나머지가 0 ~ k - 1인 애들 개수 셈
    for a in A:
        c[a % K] += 1

    ans = 1
    for i in range(1, (K + 1) // 2):
        # c[i], c[k - i]인 경우가 동시에 존재하면 안 됨 - 그래서 독립적으로 봄 - 그래서 합으로 생각
        # c[i], c[k - i]가 아예 없는 경우 : 1가지, 각각의 경우가 1개 이상 존재하는 경우가 2 ** c[i] - 1가지

        # 그리고 c[i]와 c[i + 1]은 독립적이지 않고 동시에 존재할 수 있어서 곱하기로 계산 - 왜냐하면 두 원소를 택해서 더해도 나머지가 k가 아니기 때문

        ans = ans * (pow(2, c[i], MOD) - 1 + pow(2, c[K-i], MOD) - 1 + 1) % MOD

    # 나머지가 0인 경우 고려 : 나머지가 0이면 2개 이상의 원소가 포함되었을 때 둘이 합하면 k가 되어서 안 됨
    # +1을 하는 이유는 아예 안 들어가는 경우도 있기 때문
    ans = ans * (c[0] + 1) % MOD

    # 위의 for문은 짝수일 때 n // 2인 경우를 고려하지 않음
    # 짝수일 때도 두 개 더하면 나머지가 k가 나와서 둘이 같이 존재 못함
    if K % 2 == 0:
        ans = ans * (c[K // 2] + 1) % MOD

    # 1 : 빈 집합 개수, n : 원소가 1개인 집합 개수
    ans = (ans - (N + 1)) % MOD
    print(ans)


if __name__ == "__main__":
    main()
