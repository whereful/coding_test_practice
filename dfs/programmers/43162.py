import sys
sys.setrecursionlimit(10 ** 6)


def solution(n, computers):

    def dfs(start):
        visited[start] = 1

        for next in range(n):
            if computers[start][next] == 1 and visited[next] == 0:
                dfs(next)

    visited = [0] * n

    ans = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            ans += 1

    return ans
