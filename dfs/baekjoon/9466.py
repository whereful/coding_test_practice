'''
# comment

# visited 배열을 초기화 또는 각 시작점에 대해서 독립적으로 dfs를 적용할 시 시간 초과 발생

# https://aia1235.tistory.com/47
'''


import sys


def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 6)

# 매개변수로 배열을 설정할 경우 각 dfs마다 독립적인 배열 공간 형성


def dfs(node):

    global answer

    # 이미 살펴본 점인 경우
    if visited[node] == 1:

        # 중간에 사이클이 있는 경우를 고려하여 이미 살펴본 점이 최초로 있는 점에서부터 배열을 측정하여 반영
        if node in all_list:
            # all_list[all_list.index(node):]이 진정한 사이클을 이루는 배열
            answer -= len(all_list[all_list.index(node):])
            return
        # 이 경우는 그 전에 살펴본 것이 반영된 것이므로 바로 종료해야 함
        else:
            return

    # 방문 처리
    visited[node] = 1

    # 경로 전체 추가
    all_list.append(node)

    for next in graph[node]:
        dfs(next)

    # dfs가 종료되는 중에 실행되는 코드
    # 원래는 visited[n] = 0으로 설정하여 다시 탐색해야 하지만 이 문제에서는 시간초과 발생


for _ in range(int(input())):
    n = int(input())

    # 변수명 중복 방지 설정
    temp_li = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i].append(temp_li[i - 1])

    visited = [0] * (n + 1)

    answer = n
    for i in range(1, n + 1):
        # 이미 살펴본 점을 살펴보지 않음으로써 노드 개수만큼만 살필려고 함
        # 이 코드가 없으면 시간 초과 발생

        if visited[i] == 0:

            # 최초 시작점에 해당하는 배열 선언
            all_list = []
            dfs(i)

    print(answer)
