'''
# comment

빈 방 우선순위 > 벽 우선순위
--> 빈 방들 먼저 탐색

# dijkstra[0][0] ~ dijkstra[n-1][n-1] 관점도 적용 가능

'''

'''
# answer

import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 모든 칸 탐색


def bfs(i, j):
    q = []
    # 부순 벽 개수, 좌표 삽입
    heapq.heappush(q, (0, i, j))
    visited[i][j] = 1

    while q:
        count_wall, y, x = heapq.heappop(q)

        # 목적지 도착하면 return
        if y == n - 1 and x == m - 1:
            return count_wall

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 좌표 범위 내이고 방문하지 않으면
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and \
                    visited[ny][nx] == 0:

                # 빈 방이면 벽 부수지 않고 진행
                if graph[ny][nx] == 0:
                    heapq.heappush(q, (count_wall, ny, nx))
                    visited[ny][nx] = 1
                # 벽이면 벽 부수고 진행
                elif graph[ny][nx] == 1:
                    heapq.heappush(q, (count_wall + 1, ny, nx))
                    visited[ny][nx] = 1


m, n = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(bfs(0, 0))
'''
