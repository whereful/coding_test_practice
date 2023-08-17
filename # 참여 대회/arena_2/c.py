# https://solved.ac/arena/2/editorial

import heapq
import sys


def input(): return sys.stdin.readline().strip()


N = int(input())
Q = []

# 최대값을 저장하는 변수
mx = 0

for v in map(int, input().split()):

    # 최대값 갱신
    mx = max(mx, v)

    # 최소 힙 설정
    heapq.heappush(Q, v)

# 현재 진행된 최대값을 초기 배열의 최대값으로 설정
curmx = mx

# 정답을 현재 최대값에서 최소 힙의 최소값을 뺀 값으로 설정
ans = curmx - Q[0]

# 최소값이 초기 배열의 최대값보다 작을 때까지 반복
while Q[0] < mx:

    # 최소 힙에서 최소값 추출
    v = heapq.heappop(Q)

    # 정답을 기존과 현재 설정된 최대값에서 최소값을 뺀 값과 비교
    ans = min(ans, curmx - v)

    # 현재 최대값을 기존값과 최소값의 2배와 비교
    curmx = max(curmx, 2 * v)

    # 최소힙에 최소 * 2를 삽입하여 변화 반영
    heapq.heappush(Q, 2 * v)

print(min(curmx-Q[0], ans))
