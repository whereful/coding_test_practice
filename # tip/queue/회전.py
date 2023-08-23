from collections import deque

a = [1, 2, 3, 4, 5]

b = deque(a)

# 오른쪽으로 1칸 이동
b.rotate(1)

# 왼쪽으로 1칸 이동
b.rotate(-1)
