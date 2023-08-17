'''
x + (x + 1) + ... + y == (y + x) * (y - x + 1) // 2이 성립

(y + x) * (y - x + 1) // 2 == 소수

1. y + x == 2 and y - x + 1이 소수 -> y >= 2, x >= 2라서 불가능
2. y + x == 소수 and y - x + 1 == 2 -> y = x + 1, 2x + 1이 소수

'''

import sys
def input(): return sys.stdin.readline().strip()


# 0 ~ 1000000 + 1까지 소수 판별
is_prime = [1] * (1000001 + 1)
for i in range(2, 1000001 + 1):
    if is_prime[i] == 1:
        for j in range(i * 2, 1000001 + 1, i):
            is_prime[j] = 0

# arr[i] = i + (i + 1)이 소수면 1 아니면 0, i는 L, i + 1 = R
arr = [1 if is_prime[i * 2 + 1] == 1 else 0 for i in range(0, 500000 + 1)]

# arr[i] : L = 0 ~ i일 때 소수 개수 ==> arr[7] = [0, 0 * 2 + 1]인 경우 + [1, 1 * 2 + 1]인 경우 + ...
for i in range(1, 500000 + 1):
    arr[i] += arr[i - 1]

for _ in range(int(input())):
    l, r = map(int, input().split())

    # [7, 12]를 예를 들면 [7, 8], [8, 9], ... [11, 12]가 존재
    # L = 0 ~ 11인 경우에서 L = 0 ~ 6인 경우를 제외한 경우

    print(arr[r - 1] - arr[l - 1])
