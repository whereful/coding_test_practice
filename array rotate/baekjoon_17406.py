'''
# comment

# https://jennnn.tistory.com/74

# https://www.acmicpc.net/source/28569075

'''

from itertools import permutations
from copy import deepcopy

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
rotate = [list(map(int, input().split())) for _ in range(k)]

ans = 10 ** 9

# 1. 회전 순서 정하기 (최대 6!=720)
for p in permutations(rotate, k):

    # 2. 회전
    copy_graph = deepcopy(graph)  # 원본리스트 카피

    for r, c, s in p:
        r -= 1
        c -= 1

        # 간격이 s부터 시작해서 1까지 진행함
        for i in range(s, 1 - 1, -1):

            tmp = copy_graph[r-i][c+i]

            # 제일 왼쪽, 위칸에서 시작되는 가로 막대를 오른쪽으로 밈
            copy_graph[r-i][c-i+1:(c+i) + 1] = copy_graph[r-i][c-i:c+i]  # ->

            # 제일 왼쪽, 두번째 위칸에서 시작되는 세로 막대를 위로 올림
            for y in range(r-i, r+i-1 + 1):  # ↑
                copy_graph[y][c-i] = copy_graph[y+1][c-i]

            # 두 번째 왼쪽, 제일 아래칸에서 시작되는 가로 막대를 왼쪽으로 밀기
            copy_graph[r+i][c-i:c+i-1 + 1] = copy_graph[r+i][c-i+1:c+i+1]  # <-

            # 제일 오른쪽, 두 번째 위칸에서 시작되는 세로 막대를 아래로 내리기
            for y in range(r+i, r-i+1 - 1, -1):  # ↓
                copy_graph[y][c+i] = copy_graph[y-1][c+i]

            # 최종 결과 변경 전 오른쪽 위 꼭지점 값은 한 칸 아래로 내려와야 함
            copy_graph[r-i+1][c+i] = tmp

    # 3. 각 행의 최소값 찾기
    for row in copy_graph:
        ans = min(ans, sum(row))


print(ans)
