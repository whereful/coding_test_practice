import sys

sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 모든 노드의 부모를 0번 노드로 설정
visited = [0]*(n+1)
arr = []

# dfs 방식으로 그래프로부터 트리 생성
# visited 배열을 직전 부모로 설정


def dfs(s):
    for i in graph[s]:

        if visited[i] == 0:
            visited[i] = s
            dfs(i)


dfs(1)

for x in range(2, n+1):
    print(visited[x])
