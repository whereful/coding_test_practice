'''

https://velog.io/@leehe228/boj14428
'''


import sys
from math import *

input = sys.stdin.readline
INF = sys.maxsize

# 리스트의 대소를 비교하기 위한 사용자정의 min 함수


def min(a: list, b: list) -> list:
    if a[0] > b[0]:
        return b
    else:
        return a

# 세그먼트 트리 생성 함수


def initTree(node, start, end):
    if start == end:
        segtree[node] = values[start]
        return segtree[node]

    mid = (start + end) // 2
    segtree[node] = min(initTree(node * 2, start, mid),
                        initTree(node * 2 + 1, mid + 1, end))
    return segtree[node]


# 세그먼트 트리 쿼리 함수
def query(node, start, end, left, right):
    if start > right or end < left:
        return [INF, INF]

    if left <= start and end <= right:
        return segtree[node]

    mid = (start + end) // 2
    return min(query(node * 2, start, mid, left, right), query(node * 2 + 1, mid + 1, end, left, right))


# 트리 업데이트 함수
def update(node, start, end, index, x):
    if index < start or index > end:
        return [INF, INF]

    if start == end:
        segtree[node] = x
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, x)
    update(node * 2 + 1, mid + 1, end, index, x)

    segtree[node] = min(segtree[node * 2], segtree[node * 2 + 1])


N = int(input())

temp = list(map(int, input().split()))
values = [[0, 0] for _ in range(N)]
# 입력 값을 [값, 인덱스] 형태로 변환해 리스트 저장
for i in range(N):
    values[i][0] = temp[i]
    values[i][1] = i + 1

# 세그먼트 트리 사이즈
ts = 1 << (int(ceil(log2(N))) + 1)
segtree = [0] * ts

# 트리 생성
initTree(1, 0, N - 1)

M = int(input())
for _ in range(M):
    A, B, C = map(int, input().split())

    # 트리 값 변경
    if A == 1:
        values[B - 1][0] = C
        update(1, 0, N - 1, B - 1, values[B - 1])

    # 구간 출력
    else:
        print(query(1, 0, N - 1, B - 1, C - 1)[1])
