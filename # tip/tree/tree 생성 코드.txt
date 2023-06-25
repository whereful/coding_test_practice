'''
해당 문제

백준 
15681
'''


# dfs 방식으로 그래프로부터 트리 생성
def make_tree(root):
    if visited[root] == 1:
        return

    visited[root] = 1

    for node in graph[root]:
        if visited[node] == 0:
            tree[root].append(node)
            make_tree(node)


n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# tree 생성
make_tree(r)

