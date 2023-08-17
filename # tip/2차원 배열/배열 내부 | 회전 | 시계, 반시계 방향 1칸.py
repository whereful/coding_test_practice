'''
baekjoon : 17406

'''

# 시계방향


def spin(r, c, s):

    r -= 1
    c -= 1

    # 영역을 다르게 하여 1칸 회전 반복
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

        # t3 : ey-1 ~ sy // 아래로
        for t3 in range(ey-1, sy - 1, -1):
            bd[t3+1][ex] = bd[t3][ex]

        # t4 : ex-1 ~ sx + 1 // 오른쪽으로
        for t4 in range(ex-1, sx + 1 - 1, -1):
            bd[sy][t4+1] = bd[sy][t4]

        bd[sy][sx+1] = tmp


# 반시계 방향
def spin_reverse(r, c, s):

    r -= 1
    c -= 1

    # 영역을 다르게 하여 1칸 반복
    for i in range(1, s + 1):

        # 왼쪽 위 좌표 설정
        sy, sx = r-i, c-i

        # 오른쪽 아래 좌표 설정
        ey, ex = r+i, c+i

        tmp = bd[ey][sx]

        # t3 : ey-1 ~ sy // 아래로
        for t3 in range(ey-1, sy - 1, -1):
            bd[t3+1][sx] = bd[t3][sx]

        # t2 : sx+1 ~ ex // 왼쪽으로
        for t2 in range(sx+1, ex + 1):
            bd[sy][t2-1] = bd[sy][t2]

        # t : sy+1 ~ ey  // 위로
        for t in range(sy+1, ey + 1):
            bd[t-1][ex] = bd[t][ex]

        # t4 : ex-1 ~ sx + 1 // 오른쪽으로
        for t4 in range(ex-1, sx + 1 - 1, -1):
            bd[ey][t4+1] = bd[ey][t4]

        bd[ey][sx+1] = tmp


n = int(input())
bd = [list(map(int, input().split())) for _ in range(n)]
