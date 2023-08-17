# https://www.acmicpc.net/problem/16724

# https://www.acmicpc.net/source/30941371

import sys
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())
board = [input() for _ in range(n)]
visited_by = [[-1] * m for _ in range(n)]


def get_next(r, c):
    if board[r][c] == 'U':
        return r - 1, c
    elif board[r][c] == 'D':
        return r + 1, c
    elif board[r][c] == 'L':
        return r, c - 1
    elif board[r][c] == 'R':
        return r, c + 1


ans = 0
for row in range(n):
    for col in range(m):
        if visited_by[row][col] != -1:
            continue

        num = row * m + col

        r, c = row, col
        while visited_by[r][c] == -1:
            visited_by[r][c] = num
            r, c = get_next(r, c)
        if visited_by[r][c] == num:
            ans += 1

print(ans)
