'''
# comment

# https://www.acmicpc.net/board/view/79877

# https://www.acmicpc.net/source/54560242

'''


import sys
def input(): return sys.stdin.readline().strip()


def find_parent(i):
    if parent[i] == i:
        return i
    parent[i] = find_parent(parent[i])  # 최종 부모를 직전 부모로 등록
    return parent[i]


def union(a, b):
    pa = find_parent(a)  # a의 최종 부모(직전 부모) 찾기
    pb = find_parent(b)  # b의 최종 부모(직전 부모) 찾기

    # 최종 부모끼리 연결
    if pa < pb:  # 노드 값이 더 작은 쪽을 최종 부모로 삼기
        parent[pb] = pa
    else:  # 두 가지 경우 모두 고려 필요
        parent[pa] = pb


n = int(input())

parent = [i for i in range(n + 1)]

for _ in range(n - 2):
    a, b = map(int, input().split())

    # 사이클이 발생하지 않으면 집합 합침
    if find_parent(a) != find_parent(b):
        union(a, b)

# 간선을 1번만 순회하면 부모가 제대로 설정되지 않는 오류 발생
for i in range(1, n + 1):
    find_parent(i)

for i in range(1, n - 1 + 1):
    if parent[i] != parent[i + 1]:
        print(parent[i], parent[i + 1])
        break
