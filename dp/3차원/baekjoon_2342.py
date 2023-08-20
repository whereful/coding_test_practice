# https://wondev.tistory.com/161

# 3차원 배열 모든 칸 채우기

def po(a, b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a-b) == 2:
        return 4
    else:
        return 3


INF = int(1e11)

# 1 2 2 4 0
nums = list(map(int, input().split()))
n = len(nums)

# dp[i][left][right] = Minimum of Sum of power - [ith][left foot][right foot]
dp = [[[INF] * 5 for _ in range(5)]
      for _ in range(n)]
dp[0][0][0] = 0


# 1 2 2 4 0에서 0에서는 4까지 고려한 결과를 나타냄 // nums[3]까지만 입력됨
for i in range(n - 2 + 1):
    a = nums[i]

    # 왼발, 오른발을 아예 다른 변수로 설정, 모든 경우 전부 고려
    for left in range(5):
        for right in range(5):
            dp[i+1][left][a] = min(dp[i+1][left][a], dp[i]
                                   [left][right] + po(right, a))
            dp[i+1][a][right] = min(dp[i+1][a][right],
                                    dp[i][left][right] + po(left, a))

# 2차원 배열 전체 최소값
print(min(map(min, dp[n-1])))
