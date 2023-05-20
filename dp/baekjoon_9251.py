'''
# comment

# https://myjamong.tistory.com/317
'''

s = input()
n = len(s)

p = input()
m = len(p)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == p[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[n][m])
