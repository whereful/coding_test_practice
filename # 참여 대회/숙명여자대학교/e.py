from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


def bfs(i, j, li):
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((0, i, j))
    visited[i][j] = 1

    while q:

        dis, y, x = q.popleft()

        if board[y][x] == 'F':
            li.append([y, x, dis])

        for d in dk:
            ny, nx = y + d[0], x + d[1]

            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and visited[ny][nx] == 0 and board[ny][nx] != 'D':
                q.append((dis + 1, ny, nx))
                visited[ny][nx] = 1


dk = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

S = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 'S']
H = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 'H']

SF = []
bfs(S[0][0], S[0][1], SF)

HF = []
bfs(H[0][0], H[0][1], HF)

ans = sys.maxsize

for START in SF:
    for END in HF:
        if START[0] == END[0] and START[1] == END[1]:
            ans = min(ans, START[2] + END[2])

print(ans if ans < sys.maxsize else -1)
