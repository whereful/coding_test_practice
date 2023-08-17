from collections import deque


def solution(priorities, location):
    q = deque([(i, v) for i, v in enumerate(priorities)])

    # 우선순위를 역정렬
    pri, index = sorted(priorities, reverse=True), 0

    while q:
        # 인덱스와 우선순위를 살핌
        i, v = q.popleft()

        # 우선순위가 가장 크지 않으면 큐에 다시 추가
        if v != pri[index]:
            q.append((i, v))
        else:
            # 다음 가장 큰 우선순위를 살핌, 현재 실행한 프로세스가 location이면 index 값을 리턴
            index += 1
            if location == i:
                return index
