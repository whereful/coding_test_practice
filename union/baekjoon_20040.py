'''
# comment

'''

import sys
def input(): return sys.stdin.readline().strip()


def find_parent(i):
    if i == parent[i]:
        return parent[i]
    parent[i] = find_parent(parent[i])
    return parent[i]


def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


n, m = map(int, input().split())

parent = [i for i in range(0, n - 1 + 1)]

ans = 1e11
for i in range(1, m + 1):
    a, b = map(int, input().split())

    if find_parent(a) != find_parent(b):
        union(a, b)
    else:
        # 가장 처음에 발견된 값이 최솟값
        ans = min(ans, i)

print(ans if ans != 1e11 else 0)
