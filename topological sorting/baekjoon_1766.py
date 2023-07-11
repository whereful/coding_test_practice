'''
# comment

https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-1766-%EB%AC%B8%EC%A0%9C%EC%A7%91
'''

import sys
import heapq

sys.setrecursionlimit(10 ** 8)
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
in_degree = [0 for _ in range(n + 1)]  # in_degree[x]  <-- x번 문제의 들어오는 차수
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    in_degree[b] += 1  # a->b 이므로 b의 in_degree를 하나 늘림
    graph[a].append(b)

minh = []  # 최소힙
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(minh, i)  # 최소힙에  차수가 0인 문제들를 넣어줌

# 최소힙이 빌 때까지
while minh:
    x = heapq.heappop(minh)  # 차수가 가장 낮고 문제 번호도 가장 낮은 문제를 pop
    print(x, end=" ")

    for next in graph[x]:  # 문제 x가 가리키고 있는 문제들 순회
        in_degree[next] -= 1  # 해당 문제의 차수 하나 줄임
        if in_degree[next] == 0:  # 만약 그 문제의 차수가 0이 되면, 이제 풀 수 있게 되므로 최소힙에 집어넣음
            heapq.heappush(minh, next)
