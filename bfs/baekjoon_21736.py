'''
# comment

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
            if graph[i][j] == 'I':
                sy = i
                sx = j
                break

    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 1

    # 문제의 특별한 변수 : 사람 수
    global person

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and \
                    graph[ny][nx] != 'X' and visited[ny][nx] == 0:

                if graph[ny][nx] == 'P':
                    person += 1

                q.append((ny, nx))
                visited[ny][nx] = 1

    return


n, m = map(int, input().split())

graph = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

person = 0

bfs()

print(person if person != 0 else 'TT')
