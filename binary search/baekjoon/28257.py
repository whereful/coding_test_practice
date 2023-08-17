'''
# comment

R : 문제에서 제시된 줄

RA : A번째 줄까지 있는 총 민트 초코 개수

A = 3k 이면
R(A) = 3k(k+1) // 2 - k

A = 3k + 1
R(A) = 3k(k+1) // 2 + 1

A = 3k + 2
R(A) = 3k(k+1) // 2 + 1 + k 

'''

# https://upload.acmicpc.net/4cc6c91c-4a1b-4333-a52c-736f17d890e9/

import sys
def input(): return sys.stdin.readline().strip()

# 해당 라인까지 누적된 민트 초코의 개수


def line_sum_mint(l):
    k = l // 3

    # 줄 번호가 3k, 3k+1, 3k+2인지에 따라 달라짐
    if (l % 3 == 0):
        s = 3 * k * (k + 1) // 2 - k
    elif (l % 3 == 1):
        s = 3 * k * (k + 1) // 2 + 1
    else:
        s = 3 * k * (k + 1) // 2 + 1 + k

    return s


def start_num(l):
    mo = l % 3

    if mo == 1:
        return 1
    elif mo == 2:
        return 3
    else:
        return 2


# 배열 선언 없이 특정 값 이상을 찾는 이분 탐색


def binary_search():

    # 번호가 n인 초코는 줄 번호가 4n인 줄에 무조건 포함됨
    start = 1
    end = 4 * n

    # 최종 결과 변수
    result = end

    while start <= end:
        # 찾는 줄 번호 이분탐색
        mid = (start + end) // 2

        # 줄에 해당하는 누적된 민트 초코 개수 구하기
        s = line_sum_mint(mid)

        # 해당 줄 번호까지 누적된 총 민트 초코의 개수가 찾는 초코 번호보다 크면 조건 만족
        if s >= n:
            # 최종 결과를 찾은 줄 번호로 수정
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


for _ in range(int(input())):
    n = int(input())

    line = binary_search()

    # 해당 줄에서 그 전줄까지 누적된 모든 초코 개수 + line의 나머지에 따라 달라지는 시작 번호 + 3개씩 증가하는 (총 민트초코 번호에서 해당 라인 전까지
    # 누적된 민트초코 번호를 뺀 값에다가 1을 뺀 값 - 1을 뺀 이유는 시작 번호 때문임)
    print(line * (line - 1) // 2 + start_num(line) +
          3 * (n - line_sum_mint(line - 1) - 1))
