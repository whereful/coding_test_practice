'''
# comment

# https://velog.io/@enchantee/%EB%B0%B1%EC%A4%80-1005-Python-kvth6jbu

# 모든 위상에 대해서 전부 살핌

# 위상 정렬에 대한 코드 전부 작성 후 dp 코드 적용
'''

from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):
    n, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    arr = [0] + list(map(int, input().split()))

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1

    end = int(input())

    q = deque()

    # 문제의 특별한 변수 dp
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
            # 문제의 특별한 코드
            dp[i] = arr[i]

    while q:
        node = q.popleft()

        for next in graph[node]:

            degree[next] -= 1

            # 문제의 특별한 코드
            dp[next] = max(dp[next], dp[node] + arr[next])

            if degree[next] == 0:
                q.append(next)

    print(dp[end])
