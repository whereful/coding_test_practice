'''
# comment

# https://velog.io/@dasd412/%EB%B0%B1%EC%A4%80-1043-%EA%B1%B0%EC%A7%93%EB%A7%90-%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''


import sys
def input(): return sys.stdin.readline().strip()


def find_parent(i):
    if i == parent[i]:
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


n, m = list(map(int, input().split()))

parent = [i for i in range(n + 1)]

# 진실을 아는 자의 부모를 0으로 설정
for person in list(map(int, input().split()))[1:]:
    parent[person] = 0


# 파티들 저장
parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

    # 파티의 참석한 사람들에 대해 2명씩 union 실행
    for i in range(0, len(party) - 1):
        union(party[i], party[i + 1])

# 부모가 제대로 설정되지 않을 수 있어서 부모 다시 조회
for i in range(0, n + 1):
    find_parent(i)

answer = 0

for party in parties:

    know = False
    for i in range(len(party)):
        # 파티 참가자 중 적어도 1명이 진실을 아는 사람의 집합에 속해 있으면
        if find_parent(party[i]) == 0:
            know = True
            break

    if not know:
        answer += 1

print(answer)
