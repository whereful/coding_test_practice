import sys
import heapq


def input(): return sys.stdin.readline().strip()


def dijkstra(start):
    distance = [1e11 for _ in range(n)]
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dis, node = heapq.heappop(q)

        for cost, next in graph[node]:
            if distance[next] > distance[node] + cost:
                distance[next] = distance[node] + cost
                heapq.heappush(q, (distance[next], next))

    # 거리가 작으면 아이템 개수 더함
    return sum([items[i] for i in range(n) if distance[i] <= m])


n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1].append((l, b - 1))
    graph[b - 1].append((l, a - 1))

print(max([dijkstra(i) for i in range(n)]))
