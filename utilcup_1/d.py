import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


for _ in range(int(input())):
    co = list(map(int, input().split()))

    if co[0] == 1:
        board[co[1] - 1] = [board[co[1] - 1][-1]] + board[co[1] - 1][:-1]
    else:
        board = list(map(list, zip(*board[::-1])))

for b in board:
    print(*b)
