from collections import defaultdict
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
ans = defaultdict(set)

for _ in range(n):
    a, b = map(int, input().split())

    if a == 0 and b > 0:
        ans[0].add(1)
    elif a == 0 and b < 0:
        ans[0].add(-1)

    elif a > 0:
        ans[1].add(b / a)

    elif a < 0:
        ans[-1].add(b / a)

# print(ans)
print(len(ans[0]) + len(ans[1]) + len(ans[-1]))
