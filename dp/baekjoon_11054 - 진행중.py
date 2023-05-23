'''
# comment

# https://coooco.tistory.com/104

'''

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
s = list(map(int, input().split()))

up = [1] * n
down = [0] * n

for i in range(1, n):
    for j in range(i):
        if s[j] < s[i]:
            up[i] = max(up[j]+1, up[i])

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if s[i] > s[j]:
            down[i] = max(down[j]+1, down[i])

sum = 0
for i in range(n):
    sum = max(sum, up[i]+down[i])

print(sum)
