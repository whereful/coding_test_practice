'''
# comment

크루스칼 알고리즘
'''


import sys
def input(): return sys.stdin.readline().strip()


def find_parent(i):
    if parent[i] == i:
        return parent[i]
    parent[i] = find_parent(parent[i])
    return parent[i]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

parent = [i for i in range(n + 1)]

# 크루스칼 알고리즘은 간선마다 가중치가 달라 간선을 저장해야 함
edges = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

answer = 0
for c, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a, b)
        answer += c

print(answer)
