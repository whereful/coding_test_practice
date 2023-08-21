import sys
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 6)


def dfs(node):

    for next in graph[node]:
        if parent[next] == 0:
            parent[next] = node
            dfs(next)


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)

dfs(1)

print('\n'.join(map(str, parent[2:])))
