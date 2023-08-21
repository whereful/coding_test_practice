import sys
def input(): return sys.stdin.readline().strip()


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 행은 물건의 인덱스, 열은 무게 제한
dp = [[0] * (k + 1) for _ in range(n)]

# 0번째 물건만 고려하였을 때는 물건 무게부터 가치가 설정됨
for l in range(0, k + 1):
    if l >= arr[0][0]:
        dp[0][l] = arr[0][1]

# 위 for문에서 1행을 정의하였음, 그리고 0열은 무게 제한이 0인 경우인데 이 경우는 항상 0이므로 볼 필요 없음
for i in range(1, n - 1 + 1):
    for j in range(1, k + 1):
        # 만약 i번째 물건의 무게가 제한이 넘으면
        # i번째에서 j 무게까지 고려하였을 때는 i번째 물건을 선택한 경우와 선택하지 않은 경우로 나눌 수 있음
        if j >= arr[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i][0]] + arr[i][1])
        # i번째 물건의 무게가 제한을 넘지 않으면
        # i번째 물건을 선택한다는 경우는 없음
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

# for d in dp:
#     print(d)

print(dp[n - 1][k])
