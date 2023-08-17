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

    # 기존 계층에서 점진적으로 증가한 경우 - 계층이 이동함(새로운 계층 발견)
    if d > last:
        last = d
        counter[d] = 1
        result.append(counter[d])

    elif d == last:
        last = d
        counter[last] += 1
        result.append(counter[d])

    elif d < last:
        last = d
        counter[d] += 1
        result.append(counter[d])

print(" ".join(map(str, result)))
