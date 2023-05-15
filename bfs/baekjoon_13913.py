'''
# comment

'''

from collections import deque


def bfs(start):
    q = deque()
    q.append((0, start))
    visited[start] = 1

    while q:
        dis, node = q.popleft()

        # 종료 조건
        if node == end:

            # 문자열 만들기
            answer = []
            while node != before[node]:
                answer.append(node)
                node = before[node]
            answer.append(start)
            answer = answer[::-1]

            print(dis)
            print(*answer)
            break

        # 다음 점 살펴봄
        next = node - 1
        if 0 <= next <= 100000 and visited[next] == 0:
            q.append((dis + 1, next))
            visited[next] = 1

            before[next] = node

        next = node + 1
        if 0 <= next <= 100000 and visited[next] == 0:
            q.append((dis + 1, next))
            visited[next] = 1

            before[next] = node

        next = node * 2
        if 0 <= next <= 100000 and visited[next] == 0:
            q.append((dis + 1, next))
            visited[next] = 1

            before[next] = node


start, end = map(int, input().split())

visited = [0] * (100001)

# 그 전 점을 저장하는 배열
before = [i for i in range(100000 + 1)]

bfs(start)
