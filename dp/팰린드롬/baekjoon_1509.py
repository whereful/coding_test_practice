'''
# comment

https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80

'''

import sys

sys.setrecursionlimit(10 ** 8)
def input(): return sys.stdin.readline().rstrip()


s = input()
L = len(s)


# dp[-1]을 정의하는 이유 : dp[start - 1]에서 start = 0인 경우 오류가 발생하지 않게 하기 위해
dp = [2500 for _ in range(L + 1)]
dp[-1] = 0

is_p = [[0] * L for i in range(L)]


for i in range(L):  # 길이 1 짜리 팰린드롬
    is_p[i][i] = 1

for i in range(1, L):  # 길이 2 짜리 팰린드롬 (AA, DD 같은 놈들)
    if s[i - 1] == s[i]:
        is_p[i - 1][i] = 1

for l in range(3, L + 1):  # 길이 3 ~ L 짜리 팰린드롬
    for start in range(L - l + 1):
        end = start + l - 1
        if s[start] == s[end] and is_p[start + 1][end - 1]:
            # 처음과 끝이 같고, 그 사이가 팰린드롬이면
            is_p[start][end] = 1  # start~end 도 팰린드롬

for end in range(L):
    for start in range(end + 1):

        # [start:end +1]이 펠린드롬이면
        if is_p[start][end]:

            # [0:end +1]의 최소 분할 개수는 기존 개수와 [0:start - 1 +1]의 최소 분할 개수 + 1의 최소 (+1은 [start:end +1]이 펠린드롬이기 때문)
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            # [0:end +1]의 최소 분할 개수는 기존 개수와 [0:end - 1 +1]의 최소 분할 개수 + 1의 최소 (+1은 [end:end +1]이 펠린드롬이기 때문)
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[L - 1])
