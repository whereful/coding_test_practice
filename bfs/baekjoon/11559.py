'''
# comment

# 영역 없애기

# https://www.acmicpc.net/source/53123205

'''
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(i, j, c):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    # 문제의 특별한 변수
    bomb_list = [(i, j)]

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny <= 12 - 1 and 0 <= nx <= 6 - 1 and \
                    visited[ny][nx] == 0 and graph[ny][nx] == c:
                q.append((ny, nx))
                visited[ny][nx] = 1

                # 터지는 영역 추가
                bomb_list.append((ny, nx))

    # 터져야 하는 영역을 전부 .으로 변경
    if len(bomb_list) >= 4:
        for i, j in bomb_list:
            graph[i][j] = '.'
        return 1

    return 0

# 벽돌을 떨어뜨리는 알고리즘


def fall():
    # 전체 가로에 대해서 왼쪽부터 시작
    for x in range(6):

        # 마지막 앞칸부터 위로 올라감
        for y in range(10, 0 - 1, -1):

            # 마지막 칸부터 y전까지 범위 설정
            # y를 고정시켜놓고 R_y를 마지막부터 시작해서 위로 올리는 방식으로 진행
            for R_y in range(11, y+1 - 1, -1):

                if graph[y][x] != '.' and graph[R_y][x] == '.':
                    graph[R_y][x], graph[y][x] = graph[y][x], '.'
                    break


graph = [list(input()) for _ in range(12)]
visited = [[0] * 6 for _ in range(12)]
count = 0

while True:
    # 무한 반복문 안에서 순회할 때마다 조건 판별
    # 순회할 때마다 초기화되는 변수 설정
    flag = 0
    visited = [[0] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visited[i][j] == 0:
                # bfs 진행할 때마다 flag 값 설정
                flag = max(flag, bfs(i, j, graph[i][j]))

    if flag == 0:
        print(count)
        exit(0)
    else:
        # 초기화될 때마다 결과가 달라지는 코드 설정
        count += 1
        fall()
