from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


n, m = map(int, input().split())

degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    size, *arr = list(map(int, input().split()))
    for i in range(0, len(arr) - 2 + 1):
        graph[arr[i]].append(arr[i + 1])
        degree[arr[i + 1]] += 1

q = deque()

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

answer = []
while q:
    node = q.popleft()

    answer.append(node)

    for next in graph[node]:
        degree[next] -= 1

        if degree[next] == 0:
            q.append(next)

if len(answer) != n:
    print(0)
else:
    print('\n'.join(map(str, answer)))
