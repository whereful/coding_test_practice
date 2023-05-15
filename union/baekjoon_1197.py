'''
# comment


'''

'''
# answer

import sys
def input(): return sys.stdin.readline().strip()

sys.setrecursionlimit(10 ** 6)


def find_parent(i):
    if parent[i] == i:
        return i
    parent[i] = find_parent(parent[i])
    return parent[i]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

# 간선 리스트 생성
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = min(a, b), max(a, b)
    edges.append((c, a, b))
edges.sort()


# 집합 생성
parent = [i for i in range(n + 1)]

answer = 0
for e in edges:
    union(e[1], e[2])
    answer += e[0]

print(answer)
'''
