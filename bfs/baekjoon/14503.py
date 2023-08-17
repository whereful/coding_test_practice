from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

# 현재 방향도 저장
sy, sx, direction = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(n)]

# 현재 점을 큐에 넣고 청소
q = deque()
q.append((sy, sx))

board[sy][sx] = 2
ans = 1


while q:
    y, x = q.popleft()

    # 시계 반시계 확인 필요
    for k in range(3, 0 - 1, -1):

        ny, nx = y + dy[(direction + k) % 4], x + dx[(direction + k) % 4]

        # 범위 내에 청소되지 않은 빈 방이 있으면
        if 0 <= ny <= n - 1 and 0 <= nx <= m - 1:
            if board[ny][nx] == 0:
                q.append((ny, nx))

                board[ny][nx] = 2
                ans += 1

                direction = (direction + k) % 4

                break

    # 최소 한 방향에서 청소되지 않은 빈 방이 있어 큐가 비지 않은 경우
    if q:
        continue

    # 현재 방향에서 반대 방향을 지정
    ny, nx = y + dy[(direction + 2) % 4], x + dx[(direction + 2) % 4]

    # 청소된 빈 방이면 그 쪽으로 좌표 이동
    if board[ny][nx] == 2:
        q.append((ny, nx))
    else:
        print(ans)
        break
