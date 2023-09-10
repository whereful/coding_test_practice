import sys
def input(): return sys.stdin.readline().strip()


n, m, k = map(int, input().split())
board = [input().split('1') for _ in range(n)]

ans = 0
for bb in board:
    for b in bb:
        if len(b) >= k:
            ans += (len(b) - (k - 1))

print(ans)
