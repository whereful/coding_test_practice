'''
# tree 문제는 trie로 해결할 수 없는 경우 존재

# 틀림


def make_tree(node):

    visited[node] = 1

    for next in graph[node]:
        if visited[next] == 0:
            tree[node].append(next)
            make_tree(next)


def dfs(node, w):
    if not tree[node]:
        return

    weights[node] = 0

    for next in tree[node]:
        weights[next] = w // len(tree[node])
        dfs(next, weights[next])


n, w = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
make_tree(1)

weights = [0] * (n + 1)
weights[1] = w

dfs(1, w)

print(round(w / sum([1 for w in weights if w > 0]), 10))
'''

# https://www.acmicpc.net/source/49172317

import sys
def input(): return sys.stdin.readline().rstrip()


N, W = map(int, input().split())

# 트리에서 연결된 간선의 개수 // 리프노드는 연결된 간선의 개수가 1개
tree = [0]*(N+1)
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U] += 1
    tree[V] += 1
cnt = 0
for i in range(2, len(tree)):
    if tree[i] == 1:
        cnt += 1
print(W/cnt)
