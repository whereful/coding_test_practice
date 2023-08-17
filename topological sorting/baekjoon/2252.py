from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())

degree = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()

    print(node, end=' ')

    for next in graph[node]:
        degree[next] -= 1

        if degree[next] == 0:
            q.append(next)
