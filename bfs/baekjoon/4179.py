'''
# comment

'''

from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    q = deque()

    # 불 먼저 큐에 삽입 및 방문 처리
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'F':
                q.append((1, 'F', i, j))
                visited[i][j] = 1

    # 캐릭터 시작 위치 삽입 및 방문 처리
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'J':
                q.append((1, 'J', i, j))
                visited[i][j] = 1

    while q:
        dis, c, y, x = q.popleft()

        # 종료 조건 명시 - 칸이 테두리이고 캐릭터가 J이면
        if (y == 0 or y == n - 1 or x == 0 or x == m - 1) and c == 'J':
            return dis

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 범위 내이고 방문하지 않았으며 다음 점이 .인 경우
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and \
                    visited[ny][nx] == 0 and graph[ny][nx] == '.':
                q.append((dis + 1, c, ny, nx))
                visited[ny][nx] = 1

    return 'IMPOSSIBLE'


n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(bfs())
