# https://www.acmicpc.net/source/62463567

# dfs의 특징을 확인하는 문제

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
depth = list(map(int, input().split()))

# counter : 각 계층에 존재하는 노드의 수
counter = [0] * (max(depth) + 1)

# 현재 내가 살펴보고 있는 노드의 계층, 제일 처음 계층을 0으로 설정함
last = 0
result = []

# 계층이 주어진 대로 살펴봄
for d in depth:

    # 계층이 확 증가한 경우는 dfs에서 존재하지 않음
    if d > last + 1:
        print(-1)
        exit(0)

    # 기존 계층에서 점진적으로 증가한 경우 - 계층이 이동함 - 증가한 경우는 무조건 새로운 계층임을 보장함
    if d > last:
        # 현재 계층 변경
        last = d
        # 새로운 계층에서는 일단 본인만 그 계층에 존재함
        counter[d] = 1
        result.append(counter[d])

    # 기존 계층과 같은 경우
    elif d == last:
        last = d

        # 현재 내가 머무는 계층에 존재하는 노드 수 증가
        counter[last] += 1
        result.append(counter[d])

    # 계층이 위로 올라간 경우
    elif d < last:
        last = d

        # 새로운 계층이 기존에 등장했을 수도 있고 처음일 수도 있는데 어쨌든 증가함
        counter[d] += 1

        result.append(counter[d])

print(" ".join(map(str, result)))
