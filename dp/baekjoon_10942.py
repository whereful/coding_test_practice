'''
# comment

# https://jshong1125.tistory.com/61

'''

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
a = list(input().split())
m = int(input())

dp = [[0] * n for _ in range(n)]

# 길이가 1인 경우
for i in range(n):
    dp[i][i] = 1

# 길이가 2인 경우
for i in range(n-1):
    if a[i] == a[i+1]:
        dp[i][i+1] = 1

# 길이가 3 이상인 경우
for i in range(2, n):
    for j in range(0, n - 1 - i + 1):
        # 양 끝이 같고 포함 문자열이 펠린드롬인 경우
        if a[j] == a[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(m):
    s, e = map(int, input().split())
    # s, e가 1부터 시작해서 0부터 시작으로 맞춤
    print(dp[s-1][e-1])
