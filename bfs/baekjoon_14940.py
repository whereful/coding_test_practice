'''
# comment

목표 지점 -> 출발지로 설정

'''

from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    sy = sx = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                sy = i
                sx = j
                break

    q = deque()
    q.append((0, sy, sx))
    visited[sy][sx] = 1

    # 문제의 특별한 코드 : 거리 2차원 배열 출발지 값 설정
    dis_graph[sy][sx] = 0

    while q:
        dis, y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and \
                    graph[ny][nx] == 1 and visited[ny][nx] == 0:
                q.append((dis + 1, ny, nx))
                visited[ny][nx] = 1

                # 문제의 특별한 코드 : 다음 지점의 거리값 설정
                dis_graph[ny][nx] = dis + 1


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

# 문제의 특별한 변수 - 거리 설정
dis_graph = [[0] * m for _ in range(n)]

bfs()

# 문제의 특별한 코드 - 도달할 수 없는 지점 값 설정
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dis_graph[i][j] = -1

for d in dis_graph:
    print(*d)
