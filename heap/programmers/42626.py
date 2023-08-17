'''
# my answer

import heapq


def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        
        if scoville[0] >= K:
            return answer
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second * 2)
        
        answer += 1
        
    return answer if scoville[0] >= K else -1
'''

from heapq import heapify, heappop, heappush


def solution(scoville, K):
    heapify(scoville)
    for i in range(1000000):
        try:
            # 공식 적용 전 만족 확인
            if scoville[0] >= K:
                return i
            heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
        except:
            # 공식 적용할 수 없으면 -1 리턴
            return -1
