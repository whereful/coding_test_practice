'''
# comment


dijkstra

max(min(1 -> x + x -> 1), 
min(2 -> x + x -> 2),
min(3 -> x + x -> 3), ...
min(n -> x + x -> n)

'''

import heapq
import sys

INF = 1e12


def input(): return sys.stdin.readline().strip()


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0

    while q:
        dis, node = heapq.heappop(q)

        for cost, next in graph[node]:
            if distance[start][next] > distance[start][node] + cost:
                distance[start][next] = distance[start][node] + cost
                heapq.heappush(q, (distance[start][next], next))


n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

# 문제의 특별한 변수 - distance 2차원 배열
distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dijkstra(i)

print(max([distance[i][x] + distance[x][i] for i in range(1, n + 1)]))
