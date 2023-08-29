# https://velog.io/@mechauk418/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%88%84%EC%A0%81%ED%95%A9
# https://www.acmicpc.net/source/54358586

import sys
def input(): return sys.stdin.readline().strip()


def prefix_sum(sy, sx, ey, ex):
    return dp[ey][ex] - dp[sy - 1][ex] - dp[ey][sx - 1] + dp[sy - 1][sx - 1]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - \
            dp[i - 1][j - 1] + arr[i - 1][j - 1]

for _ in range(int(input())):
    sy, sx, ey, ex = map(int, input().split())
    print(prefix_sum(sy, sx, ey, ex))
