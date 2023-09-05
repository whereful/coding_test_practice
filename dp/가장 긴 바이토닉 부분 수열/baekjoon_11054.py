'''
# comment

# https://coooco.tistory.com/104

'''

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
up_s = list(map(int, input().split()))
down_s = up_s[::-1]

# up : 가장 긴 증가하는 부분수열의 길이 저장하는 dp
# down : 가장 긴 감소하는 부분수열의 길이 저장하는 dp
up = [1] * n
down = [1] * n

for i in range(0, n - 1 + 1):
    for j in range(i + 1, n - 1 + 1):

        # 가장 긴 증가하는 부분 수열 dp 구함
        if up_s[i] < up_s[j]:
            up[j] = max(up[j], up[i] + 1)

        # 가장 긴 감소하는 부분 수열 dp 구함
        if down_s[i] < down_s[j]:
            down[j] = max(down[j], down[i] + 1)

# 바이토닉 부분 수열의 길이는 증가 + 감소 - 1임
# -1을 하는 이유는 증가의 기준값과 감소의 기준값이 중복되어 측정되기 때문
sum = max([up[i] + down[n - 1 - i] - 1 for i in range(0, n - 1 + 1)])

print(sum)
