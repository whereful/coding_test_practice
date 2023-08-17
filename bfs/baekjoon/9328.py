# https://www.acmicpc.net/source/50384147

# visited 배열 대신에 map_ 배열 값을 *로 설정하여 재방문 방지

from collections import deque, defaultdict
import sys
def input(): return sys.stdin.readline().strip()


def check(i, j):
    global que

    # 벽이면
    if map_[i][j] == '.':
        que.append((i, j))

    # 문서면
    elif map_[i][j] == '$':
        que.append((i, j))

        global res
        res += 1

    # 키이면
    elif map_[i][j].islower():
        que.append((i, j))
        key.add(map_[i][j])

        # 키에 해당하는 문에 대해서
        if map_[i][j].upper() in door:

            # 이미 본 적 있는 문 좌표에 대해서 큐에 추가
            for p, q in door[map_[i][j].upper()]:
                que.append((p, q))

    # 문이면
    elif map_[i][j].isupper():

        # 대응되는 키가 있으면 큐에 추가
        if map_[i][j].lower() in key:
            que.append((i, j))
        # 없으면 딕셔너리 목록에 좌표 추가
        else:
            door[map_[i][j]] += [(i, j)]

    # 벽으로 만들어서 재방문 방지
    map_[i][j] = '*'


for _ in range(int(input())):

    n, m = map(int, input().split())
    map_ = [list(input()) for _ in range(n)]

    # door을 처음에 아무것도 정의하지 않고 시작
    key, door = set(input()), defaultdict(list)
    res = 0

    que = deque([])

    # 양옆과 위에 있지 않은 키와 문에 대해서는 출발점으로 설정하지 않음
    # 출발점에 대해서만 고려

    # 양 옆 세로 체크
    for j in range(m):
        check(0, j)
        check(n-1, j)

    # 양 위 가로 체크
    for i in range(n):
        check(i, 0)
        check(i, m-1)

    while que:
        i, j = que.popleft()
        for p, q in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            # 범위 내이고 벽이 아니면 체크
            if 0 <= p < n and 0 <= q < m and map_[p][q] != '*':
                check(p, q)

    print(res)
