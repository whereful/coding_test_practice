from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


global board


def spin(sy, sx, ey, ex):

    tmp = board[sy][sx]

    for t in range(sy + 1, ey + 1):
        board[t - 1][sx] = board[t][sx]

    for t2 in range(sx + 1, ex + 1):
        board[ey][t2 - 1] = board[ey][t2]

    for t3 in range(ey - 1, sy - 1, -1):
        board[t3 + 1][ex] = board[t3][ex]

    for t4 in range(ex - 1, sx + 1 - 1, -1):
        board[sy][t4 + 1] = board[sy][t4]

    board[sy][sx + 1] = tmp


def spin_reverse(sy, sx, ey, ex):

    tmp = board[ey][sx]

    for t3 in range(ey - 1, sy - 1, -1):
        board[t3 + 1][sx] = board[t3][sx]

    for t2 in range(sx + 1, ex + 1):
        board[sy][t2 - 1] = board[sy][t2]

    for t in range(sy + 1, ey + 1):
        board[t - 1][ex] = board[t][ex]

    for t4 in range(ex - 1, sx + 1 - 1, -1):
        board[ey][t4 + 1] = board[ey][t4]

    board[ey][sx + 1] = tmp


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

airs = [(i, j) for j in range(m) for i in range(n) if board[i][j] == -1]

# t초 동안 확산
for _ in range(t):

    # 미세먼지 있는 지점 전부 1차원 배열에 넣기
    nodes = [(board[i][j], i, j) for j in range(m)
             for i in range(n) if board[i][j] > 0]

    for v, y, x in nodes:
        # 확산 칸 개수 저장하는 변수
        count = 0

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            # 범위 내에 있고 공기 청정기가 아니면
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and board[ny][nx] != -1:
                # 상하좌우에 기존 배열 값의 //5를 저장
                board[ny][nx] += v // 5
                count += 1

        # 원래 칸은 기존 칸으로부터 도출된 확산된 양을 제거해야 함
        board[y][x] -= (v // 5) * count

    # 범위에서 반시계 방향으로 회전
    spin_reverse(0, 0, airs[0][0], m - 1)

    # 공기청정기 부분, 그 옆칸 값 수정
    board[airs[0][0]][airs[0][1]] = -1
    board[airs[0][0]][airs[0][1] + 1] = 0

    # 범위에서 시계 방향 회전
    spin(airs[1][0], airs[1][1], n - 1, m - 1)

    # 공기 청정기 부분, 그 옆칸 수정
    board[airs[1][0]][airs[1][1]] = -1
    board[airs[1][0]][airs[1][1] + 1] = 0


# 전체 배열의 합 + 공기 청정기 -2 제외
print(sum([sum(b) for b in board]) + 2)
