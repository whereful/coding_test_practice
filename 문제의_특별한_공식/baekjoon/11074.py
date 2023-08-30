import sys
def input(): return sys.stdin.readline().strip()


n, k = map(int, input().split())

li = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0
for l in li:
    ans += k // l
    k %= l

print(ans)
