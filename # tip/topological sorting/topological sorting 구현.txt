# bfs 방식으로 구현

from collections import deque
def topological_sort():
    q = deque()

    # 시작점 정의
    # 우선순위 높은 것이 없는 노드들을 삽입
    for i in range(1, n + 1):
        if topology[i] == 0:
            # 큐에 추가
            q.append((1, i))


    while q:
        dis, node = q.popleft()

        # 우선순위를 answer 배열에 저장
        answer[node] = dis

        # 다음 노드를 살펴보기
        for next in graph[node]:

            # 우선순위를 높임
            topology[next] -= 1

            # 가장 높은 우선순위가 되면 큐에 추가
            if topology[next] == 0:
                q.append((dis + 1, next))


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 각 노드보다 우선순위가 높은 노드 개수 
topology = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 노드 연결
    graph[a].append(b)

    # 우선순위 높은 노드 개수 증가
    topology[b] += 1

answer = [0] * (n + 1)

topological_sort()

print(*answer[1:])