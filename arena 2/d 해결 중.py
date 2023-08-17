'''
# comment

https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-2357-%EC%B5%9C%EC%86%9F%EA%B0%92%EA%B3%BC-%EC%B5%9C%EB%8C%93%EA%B0%92
'''

import math
import sys

sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
def input(): return sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m


def make_seg(s, e, idx):

    if s == e:
        seg[idx] = (arr[s], arr[s])  # min, max
        return seg[idx]

    mid = (s + e) // 2

    l = make_seg(s, mid, idx * 2)
    r = make_seg(mid + 1, e, idx * 2 + 1)

    seg[idx] = (l[0] + r[0], l[0] * r[0])
    return seg[idx]


def f(s, e, idx, left, right):

    # 탐색범위 s~e

    # 밑의 if문 조건의 역을 그대로 작성하면 됨
    if e < left or right < s:  # 범위 밖
        return (1000000000, 0)

    mid = (s + e) // 2

    if left <= s and e <= right:  # 탐색 범위가 작아서 다 리턴
        return seg[idx]

    else:
        l = f(s, mid, idx * 2, left, right)
        r = f(mid + 1, e, idx * 2 + 1, left, right)
        return (min(l[0], r[0]), max(l[1], r[1]))


n = int(input())
arr = list(map(int, input().split()))

# b = math.ceil(math.log2(n)) + 1
# node_n = 1 << b
seg = [0] * (4 * n)
make_seg(0, n - 1, 1)

print(seg)
