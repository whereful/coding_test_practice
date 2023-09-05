'''
# comment

# https://wooono.tistory.com/656
# 위 링크는 모든 배열 원소를 살피지 않는 문제 발생

# https://www.acmicpc.net/board/view/75393

# https://www.acmicpc.net/board/view/84249
'''

import sys
def input(): return sys.stdin.readline().strip()


def two_pointer():

    start = 0  # 왼쪽 포인터
    res = 2e9 + 1

    for i in range(n):  # 오른쪽 포인터

        # 작거나 같은 경우

        # 문제에서 크거나 같은 경우에 대해 고려하므로 같은 경우에 대한 코드 작성
        if li[i] - li[start] == m:
            res = min(res, li[i] - li[start])

        # 큰 경우
        if li[i] - li[start] > m:
            while li[i] - li[start] > m and i > start:
                # 문제에서 크거나 같은 경우에 대해 고려하므로 큰 경우에 대한 코드 작성
                res = min(res, li[i] - li[start])
                start += 1

            # 문제에서 크거나 같은 경우에 대해 고려하므로 같은 경우에 대한 코드 작성
            if li[i] - li[start] == m:
                res = min(res, li[i] - li[start])

    print(res)


n, m = map(int, input().split())

# 연속하지 않으므로 정렬 가능
li = sorted([int(input()) for _ in range(n)])

two_pointer()
