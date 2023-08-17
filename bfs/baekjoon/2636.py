'''
# comment

둘러쌓인 것을 구현하는 코드

# https://developer-ellen.tistory.com/41

시작점이 (0, 0)으로 1개

graph[ny][nx] == 1 대신에 
graph[ny][nx] == 0 을 큐에 삽입
'''
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def count_cheese():
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count += 1
    return count


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 범위 내이고 방문하지 않은 점
            if 0 <= ny <= n - 1 and 0 <= nx <= m - 1 and \
                    visited[ny][nx] == 0:

                # 상하좌우 점이 0인 경우
                # 큐에 추가
                if graph[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

                # 상하좌우 점 중 1인 점을 발견한 경우
                # 해당 점을 0으로 설정
                elif graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    visited[ny][nx] = 1


n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

day = 1

# 0일 차를 저장
cheese_list = [count_cheese()]


while True:

    bfs(0, 0)

    # 날짜에 대응하는 치즈 개수 저장
    cheese_list.append(count_cheese())

    # 디버깅 코드

    # print()
    # for g in graph:
    #     print(g)
    # print()

    # 마지막 확인한 치즈 개수가 0개이면 종료
    if (cheese_list[-1] == 0):
        print(day)
        print(cheese_list[-2])
        exit(0)
    else:
        # 다음 날 진행, 방문 배열 초기화
        day += 1
        visited = [[0] * m for _ in range(n)]
