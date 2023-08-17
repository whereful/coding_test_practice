'''
# comment

# https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-16946-%EB%B2%BD-%EB%B6%80%EC%88%98%EA%B3%A0-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-4

'''

import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)
def input(): return sys.stdin.readline().rstrip()


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs(y, x):
    cnt = 0
    q = deque([(y, x)])
    visit[y][x] = 1
    while q:
        cy, cx = q.popleft()
        id_board[cy][cx] = area
        cnt += 1
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if in_range(ny, nx) and not visit[ny][nx] and board[ny][nx] == 0:
                visit[ny][nx] = 1
                q.append((ny, nx))

    return cnt


n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
id_board = [[0 for _ in range(m)] for _ in range(n)]
ans_board = [[0 for _ in range(m)] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

area = 0
size_of_area = {}


for i in range(n):
    for j in range(m):
        if not visit[i][j] and board[i][j] == 0:
            area += 1
            size_of_area[area] = bfs(i, j)

for i in range(n):
    for j in range(m):
        if board[i][j]:
            ans = 1  # 벽 부순 자리에 공간
            near = set()  # '서로다른' 빈 공간 집합을 위해 set 사용
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if in_range(ny, nx) and id_board[ny][nx]:
                    near.add(id_board[ny][nx])  # 빈 공간 집합의 고유 번호 넣어주기
            for id in near:
                ans += size_of_area[id]  # 해당 빈 공간 집합의 넓이 더해주기
            ans_board[i][j] = ans % 10

for i in range(n):
    for j in range(m):
        print(ans_board[i][j], end="")
    print()
