'''
# comment

# https://wooono.tistory.com/656

'''


import sys
def input(): return sys.stdin.readline().strip()


def two_pointer():

    # 투 포인터 시작 인덱스
    left = right = 0

    # 두 수의 차이가 M 이상이면서 제일 작은 수
    result = 2e9 + 1

    # 투 포인터 탐색 시작
    while left <= right and right <= n - 1:

        # 두 수의 차이가 M 미만일 경우
        if li[right]-li[left] < m:
            # 오른쪽 인덱스를 1 증가
            right += 1

        # 두 수의 차이가 M 이상일 경우
        else:
            # 두 수의 차이가 M 이상이면서 제일 작은 수를 비교한 뒤, 업데이트
            result = min(result, li[right]-li[left])
            # 왼쪽 인덱스를 1 증가
            left += 1

    # 결과 출력
    print(result)


n, m = map(int, input().split())

# 수열 저장
li = sorted([int(input()) for _ in range(n)])

two_pointer()
