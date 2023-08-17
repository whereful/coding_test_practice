'''
# comment

# https://www.acmicpc.net/source/46967309

'''

from itertools import permutations as perm

n, m, k = map(int, input().split())
bd = [list(map(int, input().split())) for _ in range(n)]
ins = [tuple(map(int, input().split())) for _ in range(k)]


def spin(r, c, s):

    r -= 1
    c -= 1

    # 간격마다 반복
    for i in range(1, s + 1):

        # 왼쪽 위 좌표 설정
        sy, sx = r-i, c-i

        # 오른쪽 아래 좌표 설정
        ey, ex = r+i, c+i

        tmp = bd[sy][sx]

        # t : sy+1 ~ ey  // 위로
        for t in range(sy+1, ey + 1):
            bd[t-1][sx] = bd[t][sx]

        # t2 : sx+1 ~ ex // 왼쪽으로
        for t2 in range(sx+1, ex + 1):
            bd[ey][t2-1] = bd[ey][t2]

        # t3 : ey-1 ~ sy
        for t3 in range(ey-1, sy - 1, -1):
            bd[t3+1][ex] = bd[t3][ex]

        # t4 : ex-1 ~ sx + 1
        for t4 in range(ex-1, sx + 1 - 1, -1):
            bd[sy][t4+1] = bd[sy][t4]

        bd[sy][sx+1] = tmp


answer = 9999
for I in perm(ins):

    # 배열 미리 저장
    tmp = [r[:] for r in bd]

    for r, c, k in I:
        spin(r, c, k)

    answer = min(answer, min([sum(r) for r in bd]))

    # 배열을 원본으로 복구
    bd = [r[:] for r in tmp]

print(answer)
