import heapq
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
q = list(map(int, input().split()))
heapq.heapify(q)

for _ in range(n - 1):
    for a in list(map(int, input().split())):
        heapq.heappush(q, a)
        heapq.heappop(q)

print(min(q))
