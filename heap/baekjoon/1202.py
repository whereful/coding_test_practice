# https://bio-info.tistory.com/195

# [튜플] 리스트를 힙으로 다룰 때 기본은 모든 원소를 오름차순으로 비교함

import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
gems = [[*map(int, input().split())] for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()
result = 0

# 힙 정렬로 만듬
tmp = []

for bag in bags:
    # 만약 (1, 64), (1, 65)가 있으면 무게 제한이 2 이하일 때까지 전부 힙에 넣음

    while gems and gems[0][0] <= bag:
        heapq.heappush(tmp, -gems[0][1])
        heapq.heappop(gems)
    # 무게 제한 이하인 것 전부 넣고 그중에서 가장 큰 거 추출해서 result에 누적함
    # 만약에 무게 제한이 10 이하인 것들도 전부 넣었는데 가치가 2 이하인 것들 중에서 가장 크면 그냥 그게 반영됨
    if tmp:
        result -= heapq.heappop(tmp)
print(result)
