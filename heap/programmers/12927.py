# https://school.programmers.co.kr/learn/courses/30/lessons/12927/solution_groups?language=python3

# (n + 1) ** 2 - n ** 2 = (n + 1)n -> 따라서 값이 큰 것을 최대한 작게 만들어야 최소화 가능

import heapq


def solution(n, works):
    # heapify로 하지 않으면 heappop할 때 가장 작은 원소가 반환되지 않음
    heapq.heapify(works := [-w for w in works])

    for i in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)

    # 최대힙을 만들어서 +나 0인 것은 무시해야 함
    return sum([w * w for w in works if w < 0])
