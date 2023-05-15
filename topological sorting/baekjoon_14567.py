'''
# comment


'''

'''
# answer

from collections import deque

# bfs 방식
def topological_sort():
    q = deque()

    for i in range(1, n + 1):
        if topology[i] == 0:
            q.append((1, i))

    
    while q:
        dis, node = q.popleft()

        # 정답 배열에 값 추가
        answer[node] = dis

        # 다음 노드 살펴봄
        for next in graph[node]:

            # 위상 감소시킴
            topology[next] -= 1

            if topology[next] == 0:
                q.append((dis + 1, next))


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
topology = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 부모, 자식 관계 정의
    graph[a].append(b)
    topology[b] += 1

answer = [0] * (n + 1)

topological_sort()

print(*answer[1:])
'''
