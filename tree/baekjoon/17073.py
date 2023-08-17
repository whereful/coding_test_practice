# tree 문제는 trie로 해결할 수 없는 경우 존재

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
