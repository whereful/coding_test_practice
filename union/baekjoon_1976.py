'''
# comment

반례 : https://www.acmicpc.net/board/view/51883

노드 여러 번 방문 가능, 경로 찾기 X

마지막 줄에 주어진 점들이 모두 한 집합이면 YES
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
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
part = [int(x) - 1 for x in input().split()]

parent = [i for i in range(n)]

edges = []

# 주어진 입력을 간선으로 바꾸기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            edges.append((i, j))

# 최소한 간선 개수만큼 조회하여 오류 없이 집합 설정하기
for _ in range(len(edges)):
    for a, b in edges:
        if find_parent(a) != find_parent(b):
            union(a, b)

answer = [parent[p] for p in part]
if len(set(answer)) == 1:
    print('YES')
else:
    print('NO')
