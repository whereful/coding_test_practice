'''
# comment

# https://my-coding-notes.tistory.com/586
'''

from collections import deque
import sys


def input(): return sys.stdin.readline().strip()


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(i, j):
    cand = []

    # 큐 생성 및 방문 처리 및 시작점으로부터의 거리와 좌표 저장
    q = deque()
    q.append((0, i, j))
    visited[i][j] = 1

    min_w = float('inf')

    while q:

        dis, y, x = q.popleft()

        # 상하좌우 점 살핌
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 범위 내이고 방문하지 않음
            if 0 <= ny <= n - 1 and 0 <= nx <= n - 1 and \
                    visited[ny][nx] == 0:

                # 물고기가 상어 사이즈와 같으면 큐에 삽입 및 방문
                if graph[ny][nx] == size:
                    q.append((dis + 1, ny, nx))
                    visited[ny][nx] = 1

                # 물고기가 상어 사이즈보다 작으면
                elif graph[ny][nx] < size:
                    if min_w == float('inf'):  # 처음 발견한 것보다 거리가 멀어지는 경우 바로 return
                        min_w = dw
                    elif dw > min_w:
                        return cand
                    cand.append((dw, ny, nx))

                q.append((dw, ny, nx))

    return cand


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

size, ate = 2, 0

ans = 0

while True:

    # 순회할 때마다 초기화되는 변수 설정

    # 시작점 찾기
    sy = sx = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                graph[i][j] = 0
                sy = i
                sx = j

    # 방문 배열 초기화
    visited = [[0] * n for _ in range(n)]
    cand = bfs(sy, sx)

    # 종료 조건 만족 판단
    if not cand:
        break

    else:

        cand.sort()
        dis, y, x = cand[0]
        ans += dis
        graph[y][x] = 0

        ate += 1
        if size == ate:
            size += 1
            ate = 0

print(ans)
