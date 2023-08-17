'''
# comment

# dfs?

# https://www.acmicpc.net/source/15744249

# https://jjuke-brain.tistory.com/65

'''

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 각 카메라가 회전하여 나올 수 있는 경우 전부 작성
directions = {
    # 1번 cctv에서 (1,)처럼 ,가 있어야 함
    # (1, )로 설정하지 않으면 dir이 1로 설정됨
    1: [(1, ), (2, ), (3, ), (0, )],
    2: [(0, 2), (1, 3)],
    3: [(0, 1), (1, 2), (2, 3), (3, 0)],
    4: [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    5: [(0, 1, 2, 3)],
}


def go(i, j, dir, detect):

    # print(dir)

    for d in dir:
        # print(d)

        y, x = i, j

        # 범위 내이고 벽이 아니면
        while 0 <= y <= n - 1 and 0 <= x <= m - 1 \
                and graph[y][x] != 6:

            # 빈 공간일 경우에 탐색해야 하는 집합에 추가
            if graph[y][x] == 0:
                detect.add((y, x))

            # 좌표 변경
            y = y + dy[d]
            x = x + dx[d]

    # go의 결과가 다음 solve의 detect_set이라서
    # return이 필요함
    return detect


def solve(k, detect_set):
    # print(detect_set)

    global ans

    # k는 0 ~ len(cameras) - 1까지 가능
    if k == len(cameras) or ans == blank:

        # ans의 최대값 갱신
        ans = max(ans, len(detect_set))
        return

    # k번째 카메라의 좌표 및 카메라 모드 꺼냄
    y, x, mode = cameras[k]

    # 카메라 모드에서 볼 수 있는 방향 다 꺼냄
    for dir in directions[mode]:

        # 1차원 집합에 대하여 깊은 복사 실행하여 독립성 유지
        # dir은 (,)로 구성됨
        temp = detect_set.copy()

        solve(k + 1, go(y, x, dir, temp))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cameras = []
blank = 0

for i in range(n):
    for j in range(m):

        # 빈 공간 개수 추가
        if graph[i][j] == 0:
            blank += 1

        # 벽이 아니면 카메라 좌표, 종류 추가
        elif graph[i][j] != 6:
            cameras.append((i, j, graph[i][j]))

ans = 0

solve(0, set())

print(blank - ans)
