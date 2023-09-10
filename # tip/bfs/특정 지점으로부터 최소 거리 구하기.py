from collections import deque

# 상하좌우, 나이트 등 여러 버전이 존재
DK = [(-1, 0), (1, 0), (0, 1), (1, 0)]


def bfs(i, j):
    q = deque()

    visited = [[0] * n for _ in range(n)]

    q.append((0, i, j))
    visited[i][j] = 1

    while q:
        dis, y, x = q.popleft()

        # 목적지에 도착한 경우
        if ():
            return dis

        for dk in DK:
            ny, nx = y + dk[0], x + dk[1]

            # 범위 내이고 방문하지 않았음
            if 0 <= ny <= n - 1 and 0 <= nx <= n - 1 and visited[ny][nx] == 0:

                # board[ny][nx]가 방문해도 되는 점일 경우
                if ():
                    q.append((dis + 1, ny, nx))
                    visited[ny][nx] = 1

    # 목적지에 도착하지 못한 경우
    return 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 특정 조건을 만족하는 시작점 - 1개밖에 존재하지 않아도 이렇게 작성
# sy, sx = [[i, j] for i in range(n) for j in range(n) if ()]로 작성 시 언팩킹 오류 발생
S = [[i, j] for i in range(n) for j in range(n) if ()]
