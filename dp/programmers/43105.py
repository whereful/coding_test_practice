'''
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5 
삼각형 대신 2차원 배열의 관점에서 문제 해결

'''


def solution(triangle):
    n = len(triangle)

    # 0 이상 9999 이하
    dp = [[-1] * n for _ in range(n)]

    dp[0][0] = triangle[0][0]

    for i in range(1, n - 1 + 1):
        # triangle의 j는 i번째까지 인덱스가 존재
        for j in range(0, i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return max(dp[n - 1])
