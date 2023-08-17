'''
# comment

'''

n = int(input())

li = list(map(int, input().split()))

# 모든 부분 수열은 최소 길이가 1임
# dp[i] : 가장 큰 값이 li[i]일 때 부분 수열의 길이
dp = [1] * n

# 시작점을 기준으로
for i in range(0, n - 1 + 1):
    # 시작점 다음부터 점진적으로 접근
    for j in range(i + 1, n - 1 + 1):

        # 시작점보다 이동하는 점이 더 큰 경우
        # dp[j]는 기존 dp[j]와 가장 큰 값이 시작점인 부분 수열에서 뒤에 li[j]를 붙이므로
        # 길이는 기존 dp[j]와 dp[i] + 1 중 최대값임
        if li[i] < li[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
