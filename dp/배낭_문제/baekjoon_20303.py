import sys
def input(): return sys.stdin.readline().strip()


def find_parent(a):
    if a == parent[a]:
        return parent[a]
    return find_parent(parent[a])


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    a, b = min(a, b), max(a, b)

    parent[b] = a

    # 추가 구문
    count_set[a] += count_set[b]
    count_set[b] = 0

    set_value[a] += set_value[b]
    set_value[b] = 0


n, m, k = map(int, input().split())

values = list(map(int, input().split()))

parent = [i for i in range(n)]

# 처음에는 자기 자신만이 집합이고 가치는 자기 자신만의 것
count_set = [1] * n
set_value = [values[i] for i in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())

    if find_parent(a) != find_parent(b):
        union(a, b)

# print(count_set)
# print(set_value)

# dp 배낭 문제
bags = [(c, v) for c, v in zip(count_set, set_value)]

dp = [[0] * (k - 1 + 1) for _ in range(len(bags))]
for l in range(0, k - 1 + 1):
    if l >= bags[0][0]:
        dp[0][l] = bags[0][1]

for i in range(1, len(bags) - 1 + 1):
    for j in range(1, k - 1 + 1):
        if j >= bags[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1]
                           [j - bags[i][0]] + bags[i][1])
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(dp[len(bags) - 1][k - 1])
