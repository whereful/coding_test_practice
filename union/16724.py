# https://www.acmicpc.net/source/30941371

import sys
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
board = [input() for _ in range(n)]

# visited의 값을 -1로 설정해서 집합에 속하지 않음을 나타냄
# visited[i][j] : 해당 칸이 소속된 집합의 번호
# parent 대신 2차원 배열로 집합 소속 설정
visited = [[-1] * m for _ in range(n)]


def get_next(r, c):
    if board[r][c] == 'U':
        return r - 1, c
    elif board[r][c] == 'D':
        return r + 1, c
    elif board[r][c] == 'L':
        return r, c - 1
    elif board[r][c] == 'R':
        return r, c + 1


def dfs(r, c, set_num, points):
    global ans

    # 사이클이 새로운 집합인 경우
    if visited[r][c] == set_num:
        ans += 1
        return
    # 사이클이 기존에 나타난 적 있는 집합인 경우
    elif visited[r][c] != -1:

        # 집합 번호를 기존 집합으로 수정
        set_num = visited[r][c]

        for p in points:
            visited[p[0]][p[1]] = set_num

        return

    # 집합에 소속되었다고 표시
    visited[r][c] = set_num

    nr, nc = get_next(r, c)
    dfs(nr, nc, set_num, points + [(nr, nc)])


ans = 0
for row in range(n):
    for col in range(m):

        if visited[row][col] == -1:
            # 집합 번호를 0부터 전체 칸 개수 - 1까지 설정
            dfs(row, col, row * m + col, [(row, col)])

print(ans)
