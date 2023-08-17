# https://www.acmicpc.net/source/52601448

from collections import deque

n, m = map(int, input().split())
q = deque([i for i in range(1, n + 1)])

arr = list(map(int, input().split()))

answer = 0
for a in arr:

    if q[0] == a:
        q.popleft()
        continue

    idx = q.index(a)

    answer += min(idx, len(q) - idx)

    if idx < len(q) - idx:
        for _ in range(idx):
            q.append(q.popleft())
        # q = q[x + 1:] + q[:x]
    else:
        for _ in range(len(q) - idx):
            q.appendleft(q.pop())
        # q = q[:x] + q[x + 1:]

    q.popleft()


print(answer)
