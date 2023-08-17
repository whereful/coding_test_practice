'''
https://www.acmicpc.net/source/64112279

https://chanhuiseok.github.io/posts/baek-28/

https://blog.naver.com/occidere/221085858307

https://blogshine.tistory.com/120

'''

import sys
import heapq
def input(): return sys.stdin.readline().strip()


N = int(input())

arr = []
for i in range(N):
    s, e = map(int, input().split())
    if s > e:
        s, e = e, s
    arr.append((s, e))

# 끝이 작은 순서대로 정렬한다 - 끝이 작으면 시작점이 작은 것이 앞에 온다
arr.sort(key=lambda x: x[1])

d = int(input())

answer = 0
heap = []

for start, end in arr:

    # 시작점을 넣음
    heapq.heappush(heap, start)

    # 끝점은 고정함, 조건이 맞을 때까지 시작점을 힙에서 꺼냄
    while heap and end-heap[0] > d:
        heapq.heappop(heap)

    answer = max(answer, len(heap))

print(answer)
