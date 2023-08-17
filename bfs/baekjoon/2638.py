'''
# comment

'''

from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 1

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 범위 내이고
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1:

                # 공기이고 방문하지 않았으면 큐에 추가 및 방문 처리
                if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

                # 멀쩡하거나 덜 녹은 치즈라면
                if graph[ny][nx] > 0:

                    # 녹임
                    graph[ny][nx] -= 0.5

                    # 녹인 결과 완전히 녹으면 방문처리하여 큐에 추가되지 않도록 함
                    if graph[ny][nx] == 0:
                        visited[ny][nx] = 1


def count_cheese():
    count = 0

    for i in range(n):
        for j in range(m):
            # 멀쩡한 치즈, 덜 녹은 치즈의 개수 세기
            if graph[i][j] != 0:
                count += 1

    return count


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 날짜 저장 코드
day = 0

while True:
    # ====== 반복될 때마다 초기화되는 코드 저장 ======
    day += 1

    # 덜 녹은 치즈를 멀쩡한 치즈로 치환
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0.5:
                graph[i][j] = 1

    visited = [[0] * m for _ in range(n)]
    # ==============================

    # 치즈 내부는 조회하면 안 되므로 외부의 점에 대해서 bfs 진행
    bfs(0, 0)

    # 전부 녹았는지 확인
    if count_cheese() == 0:
        print(day)
        break

    # for g in graph:
    #     print(g)
    # print()
    # print()
