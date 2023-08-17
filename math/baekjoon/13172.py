# https://www.acmicpc.net/source/58843879

# https://www.acmicpc.net/source/59772341

import sys
def input(): return sys.stdin.readline().rstrip('\n')


sys.setrecursionlimit(10**4 * 3)

MOD = 10**9+7

ans = 0
for __ in range(int(input())):
    n, s = map(int, input().split())
    ans += pow(n, MOD - 2, MOD) * s % MOD
print(ans % MOD)
