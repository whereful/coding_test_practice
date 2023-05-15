'''
# comment

'''

'''
# answer

from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 6)


def make_tree(root):
    if visited[root] == 1:
        return

    visited[root] = 1

    for node in graph[root]:
        if visited[node] == 0:
            tree[root].append(node)
            make_tree(node)


# 재귀 방식

def node_count(root):
    if tree[root] == []:
        answer[root] = 1
        return 1

    sum = 1
    for node in tree[root]:
        answer[node] = node_count(node)
        sum += answer[node]

    answer[root] = sum
    return sum

# bfs 방식
# 시간 초과


def node_count_bfs(root):

    q = deque()
    q.append(root)

    result = 0
    while q:
        node = q.popleft()

        result += 1

        for next in tree[node]:
            q.append(next)

    return result


n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# tree 생성
make_tree(r)


answer = [0] * (n + 1)

node_count(r)

for _ in range(q):
    print(answer[int(input())])
'''
