'''
# comment

# 가장 긴 증가하는 부분 수열의 결과를 뒤집으면 됨

'''

n = int(input())
li = list(map(int, input().split()))[::-1]

dp = [1] * n

for i in range(0, n - 1 + 1):
    for j in range(i + 1, n - 1 + 1):
        if li[i] < li[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
