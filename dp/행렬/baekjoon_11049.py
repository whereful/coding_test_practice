# https://velog.io/@js43o/%EB%B0%B1%EC%A4%80-11049%EB%B2%88-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C

# dp[i][j]를 정의내리기

import sys


def input(): return sys.stdin.readline().strip()


MAX = 2**32

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]  # (N × N) 2차원 배열, 대각선의 값은 자동으로 0으로 설정됨

for offset in range(1, N):  # offset = start와 end의 차이
    for start in range(0, N - offset):
        end = start + offset  # [start, end] 범위 내의 행렬들에 대한 곱셈의 최솟값 구하기

        if offset == 1:  # 두 행렬 간 곱셈일 때
            dp[start][end] = mat[start][0] * \
                mat[start][1] * mat[end][1]  # 단순 행렬곱 연산 횟수

        dp[start][end] = MAX
        for mid in range(
            start, end
        ):  # 가능한 분할 지점을 순회함. ex) ABCD => A(BCD), AB(CD), (ABC)D
            dp[start][end] = min(
                dp[start][end],
                dp[start][mid]
                + dp[mid + 1][end]
                + mat[start][0] * mat[mid][1] * mat[end][1],
            )  # 각각의 곱셈 연산 최솟값에 두 행렬곱의 연산 횟수를 더함

print(dp[0][N - 1])
