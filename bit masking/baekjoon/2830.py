# https://gukin.tistory.com/14
# https://hseungho.tistory.com/23
# https://velog.io/@studyhard/ps-boj-2830

'''
3 | 011
5 | 101
7 | 111

011 ^ 101 + 011 ^ 111 + 101 ^ 111을 (011 ^ 101) 이렇게 묶음 단위로 계산할 필요 없음

2**2의 자리수 : (0 ^ 1), (1 ^ 1), (1 ^ 1)
2**1의 자리수 : (1 ^ 0), (1 ^ 1), (0 ^ 1)
2**0의 자리수 : (1 ^ 1), (1 ^ 1), (1 ^ 1)

각 ^의 합에다가 자리수를 곱하면 10진수로 바꿀 수 있다
즉, 합을 2진수로 바꿔서 다시 10진수로 바꿀 필요 없이 바로 각 자리수 단위를 곱하면 된다

n개의 숫자가 주어지면 각 자리에는 0, 1이 a, b개 존재 -> (a + b) = n 성립
예를 들어 2**0 자리수에 0이 a개, 1이 b개 존재하면 (0 0 0 0 0 0 ... 1 1 1 1 1 ...) 이렇게 존재
여기서 2개를 선택해야 함 - 그런데 xor값이 1이 되기 위해서는 (0, 1) 조합을 선택해야 함

그래서 a * b가 성립함


'''

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = [int(input()) for _ in range(n)]

# 2**20 > 1000000이므로 넉넉하게 이진수 자리 20자리 배정
count_1 = [0] * (21)

for a in arr:
    k = bin(a)[2:][::-1]

    for i in range(len(k)):
        count_1[i] += (k[i] == '1')

answer = 0
for i in range(21):
    answer += count_1[i] * (n - count_1[i]) * pow(2, i)

print(answer)
