'''
# comment

# https://www.acmicpc.net/source/61437435

bisect 함수의 중요성
'''

import sys
import bisect


def input(): return sys.stdin.readline().strip()


N, Q = map(int, input().split())
S = input()

R = []
B = []

# 배열을 2개를 선언
for i in range(N):
    c = S[i]
    if c == 'R':
        R.append(i)
    elif c == 'B':
        B.append(i)

for _ in range(Q):
    l, r = map(int, input().split())

    # 2개의 r 중에서 인덱스가 작은 r을 구할려고 함
    # bisect_left는 찾는 값과 일치하지 않는 값의 인덱스도 반환
    # bisect_left는 l 이상인 값 중 가장 작은 값의 인덱스를 반환
    r1 = bisect.bisect_left(R, l)

    # 반환된 r1이 R 배열의 마지막 원소 이상이면 r 개수가 1개 이상이거나 0이므로 종료
    if r1 >= len(R)-1:
        print(-1)
        continue

    # 2개의 b 중에서 인덱스가 가장 큰 값을 구할려고 함
    # bisect_right - 1은 r 이하인 값 중에서 가장 큰 값의 인덱스를 반환
    b2 = bisect.bisect_right(B, r) - 1

    # 해당 인덱스가 0 이하인 경우 b의 개수는 1개 이하라서 조건이 성립하지 않음
    if b2 <= 0:
        print(-1)
        continue

    # r 중에서 큰 원소의 인덱스가 b 중에서 작은 원소의 인덱스보다 이상인 경우 조건 성립하지 않음
    if R[r1+1] >= B[b2-1]:
        print(-1)
        continue

    print(R[r1], R[r1+1], B[b2-1], B[b2])
