'''
# comment

https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-10775-%EA%B3%B5%ED%95%AD
'''

import sys

sys.setrecursionlimit(10 ** 8)
def input(): return sys.stdin.readline().rstrip()


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


def union(v1, v2):  # v1 < v2
    r1 = find(v1)
    r2 = find(v2)
    root[r2] = r1


G = int(input())
P = int(input())

root = [i for i in range(G + 1)]

ans = 0
for i in range(1, P + 1):
    gate_range = int(input())

    # 예시 1에서 맨 처음 4번 게이트에 도킹하려고 했을 때 아무 비행기도 없으니 4번 자체를 반환
    docking_loc = find(gate_range)

    # 도킹시킬 위치가 0번인 것은 1 ~ 해당 입력 번호까지 전부 비행기가 도킹되었다는 의미
    # 해당 입력에서 도킹시킬 위치가 없어도 다음 비행기는 도킹시킬 수 있음(예 : 1 ~ 5번이 전부 도킹되어도 100번은 비었을 수 있음)
    if docking_loc == 0:
        break
    ans += 1

    # 4번이 도킹되었으니 이제 가능한 도킹 위치는 3번임을 명시 - 가능한 오른쪽에서 왼쪽으로 확장하는 방식으로 진행
    union(docking_loc - 1, docking_loc)
print(ans)
