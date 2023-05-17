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

    # 물 먼저 큐에 삽입 및 방문 처리
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                q.append((1, '*', i, j))
                visited[i][j] = 1

    # 캐릭터 시작 위치 삽입 및 방문 처리
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                q.append((1, '@', i, j))
                visited[i][j] = 1

    while q:
        # print(q)

        dis, c, y, x = q.popleft()

        # 좌표가 배열 테두리에 존재 및 캐릭터가 @이면 종료
        if (y == 0 or y == n - 1 or x == 0 or x == m - 1) and c == '@':
            return dis

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 범위 내이고 방문 안 했고 다음 점이 .이면
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and \
                    visited[ny][nx] == 0 and graph[ny][nx] == '.':
                q.append((dis + 1, c, ny, nx))
                visited[ny][nx] = 1

    # while 문 내에서 종료되지 않으면 빌딩 탈출 불가
    return 'IMPOSSIBLE'


for _ in range(int(input())):
    m, n = map(int, input().split())

    graph = [input() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    print(bfs())
