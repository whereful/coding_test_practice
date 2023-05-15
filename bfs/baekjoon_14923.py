'''
# comment

# 벽을 1번만 부술 수 있다

# 예시 따라 우선순위 변경(최소 거리 -> 최소 벽 부순 개수)

# 2차원 배열에서는 우선순위가 고정되어야 함
'''

from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 우선순위가 고정되어야 함


def bfs():
    q = deque()
    # 거리, 벽을 부순 횟수(z 좌표), y, x좌표 저장
    q.append((0, 0, sy, sx))
    visited[0][sy][sx] = 1

    while q:
        dis, z, y, x = q.popleft()

        if y == ey and x == ex:
            return dis

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 범위 내이고 방문하지 않았다면
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and \
                    visited[z][ny][nx] == 0:

                # 다음 점이 벽이 아니면 그대로 삽입 및 방문 처리
                if graph[ny][nx] == 0:
                    q.append((dis + 1, z, ny, nx))
                    visited[z][ny][nx] = 1

                # 다음 점이 벽이고 벽을 부순 횟수가 0이면
                elif graph[ny][nx] == 1 and z == 0:
                    # 벽을 부순 횟수 증가 후 삽입 및 방문 처리
                    # 경로를 독립된 공간에 저장 - 우선순위가 다르기 때문에
                    q.append((dis + 1, z + 1, ny, nx))
                    visited[z+1][ny][nx] = 1

    return -1


n, m = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1
sx -= 1
ey, ex = map(int, input().split())
ey -= 1
ex -= 1

graph = [list(map(int, input().split())) for _ in range(n)]
# 부순 벽 개수 종류만큼 새로운 range 생성
visited = [[[0] * m for _ in range(n)] for _ in range(2)]

print(bfs())
