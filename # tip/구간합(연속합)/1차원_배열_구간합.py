# arr 기준으로 인덱스 설정
# arr[a] + ... + arr[b]
def prefix_sum(a, b):
    if a == 0:
        return dp[b]
    return dp[b] - dp[a - 1]


arr = list(map(int, input().split()))

# dp[i] = arr[0] + ... + arr[i]
dp = [arr[0]] * len(arr)
for i in range(1, len(arr) - 1 + 1):
    dp[i] = dp[i - 1] + arr[i]

print(dp)

# arr[1] + ... + arr[3]
print(prefix_sum(1, 3))
