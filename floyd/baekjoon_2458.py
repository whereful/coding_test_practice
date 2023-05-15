'''
# comment

# https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-2458%EB%B2%88-%ED%82%A4-%EC%88%9C%EC%84%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''

n, m = map(int, input().split())
floyd = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # a->b로 가는 길이 있으면 1로 설정
    floyd[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # i -> j로 가는 길이 없을 때 i->k, k->j로 가는 길이 있으면 i->j로 가는 길 존재
            if floyd[i][j] == 0:
                if floyd[i][k] == 1 and floyd[k][j] == 1:
                    floyd[i][j] = 1

# for f in floyd:
#     print(f)

result = 0

# 2차원 배열 가로선 + 세로선 값 구하기
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        sum += floyd[i][j] + floyd[j][i]
    result += (sum == n - 1)
print(result)
