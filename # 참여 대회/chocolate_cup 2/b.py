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

    global lands

    part_count = 1

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if 0 <= ny <= 3 - 1 and 0 <= nx <= 3 - 1 and \
                    graph[ny][nx] == 'O' and visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = 1

                part_count += 1

    lands.append(part_count)


for _ in range(int(input())):
    graph = [input() for _ in range(3)]
    visited = [[0] * 3 for _ in range(3)]

    n_and_count = list(map(int, input().split()))
    n, count_arr = n_and_count[0], n_and_count[1:]

    lands = []

    for i in range(3):
        for j in range(3):
            if graph[i][j] == 'O' and visited[i][j] == 0:
                bfs(i, j)

    if n == len(lands) and count_arr == sorted(lands):
        print(1)
    else:
        print(0)
