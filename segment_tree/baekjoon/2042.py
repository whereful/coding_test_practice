'''
# comment

https://velog.io/@heyoni/2042


https://upcount.tistory.com/12

https://velog.io/@yoopark/baekjoon-2042
'''

# Using Segment Tree

from math import ceil, log
import sys
def input(): return sys.stdin.readline().rstrip()


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

H = ceil(log(N, 2)+1)
tree = [0] * (2 ** H)

# node가 지칭하고 있는 구간이 [l, r]이다.


def init(l, r, node):
    if l == r:
        tree[node] = arr[l]
        return
    mid = (l+r) // 2
    init(l, mid, node*2)
    init(mid+1, r, node*2+1)
    tree[node] = tree[node*2] + tree[node*2+1]


init(0, N-1, 1)

# arr[IDX]를 DIFF만큼 변경했을 때의 tree 변경


def update(l, r, node, IDX, DIFF):

    # idx가 범위에 없으면 종료
    if not (l <= IDX <= r):
        return
    tree[node] += DIFF

    if l == r:
        return
    mid = (l+r) // 2
    update(l, mid, node*2, IDX, DIFF)
    update(mid+1, r, node*2+1, IDX, DIFF)

# [LEFT, RIGHT]의 구간 합을 구함.


def interval_sum(l, r, node, LEFT, RIGHT):
    if r < LEFT or RIGHT < l:  # [l, r]이 [LEFT, RIGHT]를 완전히 벗어남.
        return 0
    if LEFT <= l and r <= RIGHT:  # [l, r]이 [LEFT, RIGHT] 안에 완전히 포함됨.
        return tree[node]
    mid = (l+r) // 2
    return interval_sum(l, mid, node*2, LEFT, RIGHT) + interval_sum(mid+1, r, node*2+1, LEFT, RIGHT)


for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        update(0, N-1, 1, b, c-arr[b])
        arr[b] = c  # arr도 갱신해주는 이유는... 오로지 diff 계산할 때 필요해서
    else:
        b -= 1
        c -= 1
        print(interval_sum(0, N-1, 1, b, c))
