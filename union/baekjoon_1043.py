'''
# 연결 여부

# 세 집합 부모 동시 설정

# 부모 설정을 최소한 간선 개수만큼 해야 함

'''


def find_parent(i):
    if parent[i] == i:
        return parent[i]
    parent[i] = find_parent(parent[i])
    return parent[i]

# 한 간선에 대하여 union


def union(ed):
    min_parent = min(parent[e] for e in ed)

    for e in ed:
        parent[e] = min_parent


n, m = map(int, input().split())


parent = [i for i in range(n + 1)]

# 진실을 아는 사람의 부모를 0으로 설정
for i in list(map(int, input().split()))[1:]:
    parent[i] = 0

# 파티에서 간선들 추가
edges = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    edges.append(party)

# 부모 설정하기
for _ in range(m):
    for ed in edges:
        union(ed)

answer = 0
for ed in edges:
    min_parent = min(parent[e] for e in ed)

    if min_parent != 0:
        answer += 1

print(answer)
