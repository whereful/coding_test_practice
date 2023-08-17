from collections import defaultdict

import heapq
import sys
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):
    min_q, max_q, dic = [], [], defaultdict(int)

    for _ in range(int(input())):
        command, num = input().split()
        num = int(num)

        if command == 'I':
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
            dic[num] += 1

        elif num == -1:
            while min_q and dic[min_q[0]] == 0:
                heapq.heappop(min_q)

            if min_q:
                dic[min_q[0]] -= 1

        elif num == 1:
            while max_q and dic[-max_q[0]] == 0:
                heapq.heappop(max_q)

            if max_q:
                dic[-max_q[0]] -= 1

    answer = []

    while max_q and dic[-max_q[0]] == 0:
        heapq.heappop(max_q)

    if max_q:
        answer.append(-max_q[0])

    while min_q and dic[min_q[0]] == 0:
        heapq.heappop(min_q)

    if min_q:
        answer.append(min_q[0])

    print(' '.join(map(str, answer)) if answer else 'EMPTY')
