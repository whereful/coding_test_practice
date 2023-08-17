'''
# comment

# https://velog.io/@hysong/%EB%B0%B1%EC%A4%80-5525-IOIOI-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
'''

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
m = int(input())
s = input()

# 시작점과 끝점이 같은 투 포인터
left, right = 0, 0
answer = 0


# 끝점이 전체 인덱스 범위 내인 경우
while right <= m - 1:

    # 끝점에서 2칸 뒤가 ioi면
    if s[right:right + 2 + 1] == 'IOI':

        # 끝점 확장
        right += 2

        # 확장했을 때 p(n)이면
        if right - left == 2 * n:
            # 정답 증가
            answer += 1
            # 시작점 2칸 증가[다시 정답이 증가하는지 확인해야 하므로]
            left += 2

    # 2칸 뒤가 ioi가 아니면 - 시작점, 끝점을 다음점으로 설정
    else:
        left = right = right + 1

print(answer)
