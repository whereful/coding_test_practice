from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


n, m, x, y = map(int, input().split())

values = list(map(int, input().split()))

graph = [[] for _ in range(n)]

# 아예 방문하지 않으면 -1로 설정
visited = [-1] * n

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = deque()
for start in list(map(lambda x: int(x) - 1, input().split())):
    q.append((0, start))
    visited[start] = 1

while q:
    depth, node = q.popleft()

    # 가중치를 계층(방문 순서)과 기존 가중치를 곱한 값으로 설정함
    values[node] = depth * values[node]

    for next in graph[node]:
        if visited[next] == -1:
            q.append((depth + 1, next))
            visited[next] = 1

# 아예 방문하지 않았는데 가중치가 있는 경우 -값이 설정됨
result = sorted([v * visit for v, visit in zip(values, visited)], reverse=True)

# -값이 있는 경우 무한 해킹 가능, 아니면 합이 가장 큰 것들만 계산해서 반환
print(sum(result[:x]) if result[-1] >= 0 else -1)
