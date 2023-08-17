# https://soohyun6879.tistory.com/136

import heapq


def solution(jobs):

    # now : 현재 시간
    answer, now, i = 0, 0, 0

    # 이전에 작업을 완료한 시간
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0:  # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)

            # 현재 작업을 처리하였으므로 now로 처리
            start = now

            # now는 작업 시간 만큼 더함
            now += cur[0]

            # 작업 요청시간부터 종료시간까지의 시간 계산
            answer += now - cur[1]
            i += 1

        else:  # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1

    return answer // len(jobs)
