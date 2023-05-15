'''
# comment

# https://ddingmin00.tistory.com/59

# https://modziw.tistory.com/563

# 이미 방문한 점을 다시 살펴야 하는 경우
# 방문 처리 되었다 = 그 점으로 언제든지 다시 갈 수 있다
# 문제 예시 : (0, 2)에서 (1, 0)칸에 불이 켜짐, 따라서 (1, 0)칸 상하좌우에 방문한 점이 존재(= 그 점으로 갈 수 있는 경로가 존재)
하면 (1, 0)칸을 큐에 넣으면 됨

'''

from collections import defaultdict, deque
import sys
def input(): return sys.stdin.readline().strip()


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs():
    q = deque()

    # 시작점을 큐에 넣고 방문처리함
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        # 현재 점 살핌
        y, x = q.popleft()

        # 특별한 코드
        # 현재 위치에서 불을 킬 수 있는 곳 찾아서 불 키기
        for a, b in info[(y, x)]:
            # 불이 0이다 = 방문을 아직 하지 않았다
            if graph[a][b] == 0:
                graph[a][b] = 1

                # 현재 점에서 적용 결과 불이 켜진 점 주위에 최소 한 점이 방문처리되었으면(= 그 점으로 갈 수 있는 경로가 있으면)
                # 불이 켜진 점을 큐에 삽입 및 방문 처리
                for k in range(4):
                    na = a + dy[k]
                    nb = b + dx[k]

                    if 0 <= na <= n - 1 and 0 <= nb <= n - 1 and \
                            visited[na][nb] == 1:
                        q.append((a, b))
                        visited[a][b] = 1
                        break

        # 현재 위치에서 상하좌우를 살펴 방문처리하지 않고 불이 켜져 있으면 큐에 삽입 및 방문처리한다.
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny <= n - 1 and 0 <= nx <= n - 1 and \
                    visited[ny][nx] == 0 and graph[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = 1


n, m = map(int, input().split())
info = defaultdict(list)

graph = [[0] * n for _ in range(n)]
graph[0][0] = 1

visited = [[0] * n for _ in range(n)]

# defaultdict를 통해 불을 키고 끌 수 있는 방의 묶음을 담아준다
for _ in range(m):
    y, x, a, b = map(int, input().split())
    info[(y - 1, x - 1)].append((a - 1, b - 1))

bfs()
# graph의 1의 합을 계산하여 출력
print(sum(sum(graph, [])))
