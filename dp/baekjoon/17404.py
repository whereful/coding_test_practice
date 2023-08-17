'''
# comment

# https://lcyking.tistory.com/43

'''

INF = 1e11

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[INF, INF, INF] for _ in range(n)]

# 가장 큰 값을 정답으로 설정
ans = INF

# 시작점을 [0][i]로 설정
for i in range(3):

    # 시작점이 변경될 때마다 매번 dp table 초기화
    dp = [[INF, INF, INF] for _ in range(n)]
    
    # 시작점의 값만 원래 값으로 설정
    dp[0][i] = graph[0][i]

    # dp 공식 적용
    for j in range(1, n):
        dp[j][0] = graph[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = graph[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = graph[j][2] + min(dp[j-1][0], dp[j-1][1])


    '''
    3
    1 100 100
    100 100 100
    1 100 100
    
    ans = min(ans, min(dp[n - 1]))을 하면 위 예시처럼 시작과 끝이 같을 때 최소인 경우가 반영됨

    시작과 끝이 같은 경우 제외시켜야 함
    '''

    for j in range(3):
        if i != j:
            ans = min(ans, dp[n - 1][j])

print(ans)