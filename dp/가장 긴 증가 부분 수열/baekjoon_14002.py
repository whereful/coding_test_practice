n = int(input())
li = list(map(int, input().split()))

dp = [1] * n

for i in range(0, n - 1 + 1):
    for j in range(i + 1, n - 1 + 1):
        if li[i] < li[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))

print(dp)

ans = []
idx = max(dp)

for i in range(n - 1, 0 - 1, -1):
    if dp[i] == idx:
        ans.append(li[i])
        idx -= 1

print(*reversed(ans))
