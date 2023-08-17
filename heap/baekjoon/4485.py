'''
# 비용 최소
# 거리 최소 X

# dijkstra[0][0] ~ dijkstra[n-1][n-1] 관점도 적용 가능

'''

import heapq
import sys
def input(): return sys.stdin.readline().strip()


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(i, j, n):
    q = []
    heapq.heappush(q, (graph[i][j], i, j))
    visited[i][j] = 1

    while q:
        cost, y, x = heapq.heappop(q)

        if y == n - 1 and x == n - 1:
            return cost

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if 0 <= ny <= n - 1 and 0 <= nx <= n - 1 and \
                    visited[ny][nx] == 0:
                heapq.heappush(q, (cost + graph[ny][nx], ny, nx))
                visited[ny][nx] = 1


test = 1
while (n := int(input())) > 0:
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    # 출력 형식 주의 - 오류 시 틀렸습니다 결과 도출
    print('Problem %d: %d' % (test, bfs(0, 0, n)))
    test += 1
