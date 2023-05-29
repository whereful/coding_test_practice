'''
해당 문제

백준
2688
9446

'''


import sys
sys.setrecursionlimit(10 ** 6)


def input(): return sys.stdin.readline().strip()


# li는 최초 dfs와 자식 dfs들이 모두 공유
def dfs(start, node, count, li):

    global answer

    # 문제의 특별한 코드 - for문에 작성하지 않고 for문 전에 작성

    # 방문하지 않은 점을 방문 처리
    visited[node] = 1

    for next in graph[node]:

        # dfs는 for문 내에서 조건을 적지 않고 for문 전에 조건을 작성
        dfs(start, next, count + 1, li + [next])

    # dfs문이 종료되고 부모 dfs로 돌아가기 전에 적용해야 하는 코드
    # dfs에서 살펴본 점들을 다시 False로 설정
    # 전체 dfs문이 종료된 후 visited = [0] * (n + 1)로 초기화하는 것과 결과 동일
    visited[node] = 0


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 인덱스와 값이 같아도 자식으로 추가
for i in range(1, n + 1):
    graph[i].append(int(input()))


# 정답 배열 설정
answer = []

# 모든 점에 대해서 dfs 진행
for i in range(1, n + 1):
    dfs(i, i, 0, [i])

    # 이렇게 작성 시 n이 커질 경우 시간복잡도가 기하급수적으로 증가
    # visited = [0] * (n + 1)