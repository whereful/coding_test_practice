from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()


n, m, q = map(int, input().split())

rows = defaultdict(int)
cows = defaultdict(int)

for _ in range(q):
    a, b, v = map(int, input().split())

    if a == 1:
        rows[b - 1] += v
    else:
        cows[b - 1] += v

board_row = [[0] * m if i not in rows else [rows[i]] * m for i in range(n)]
board_cow = [[0] * n if j not in cows else [cows[j]] * n for j in range(m)]
board_cow = list(zip(*board_cow))

# for b in board_row:
#     print(b)

# print()

# for b in board_cow:
#     print(b)

for i in range(n):
    for j in range(m):
        print(board_row[i][j] + board_cow[i][j], end=" ")
    print()
