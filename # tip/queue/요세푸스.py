from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n + 1)])

# print(q)
ans = []

for _ in range(n):
    # 제거해야 할 원소 제외하고 k % 길이만큼 왼쪽으로 이동(앞의 것을 뒤로 보내야 하기 때문)
    q.rotate(-(k % len(q) - 1))
    ans.append(q.popleft())

print("<" + ', '.join(map(str, ans)) + ">")
