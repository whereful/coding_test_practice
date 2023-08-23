from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])

# print(q)
ans = []

for _ in range(n):
    q.rotate(-(k % len(q) - 1))
    ans.append(q.popleft())

print("<" + ', '.join(map(str, ans)) + ">")
