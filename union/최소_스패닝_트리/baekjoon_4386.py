from math import sqrt


def dis(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_parent(a):
    if a == parent[a]:
        return parent[a]
    parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

points = [list(map(float, input().split())) for _ in range(n)]

distances = sorted([(dis(points[i], points[j]), i, j)
                    for i in range(n) for j in range(i + 1, n)])

# print(distances)

ans = 0.0
parent = [i for i in range(n)]

for d, a, b in distances:
    if find_parent(a) != find_parent(b):
        union(a, b)

        ans += d

        # print(a, b, ans)

print(round(ans, 2))
