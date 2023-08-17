'''
# comment

# https://jaehwaseo.tistory.com/49

# https://heytech.tistory.com/79

# https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98python%EB%B0%B1%EC%A4%80-2143%EB%91%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9

'''


from bisect import bisect_left, bisect_right
import sys
def input(): return sys.stdin.readline().strip()


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

pA, pB = [], []
for i in range(0, n - 1 + 1):
    for j in range(i, n - 1 + 1):
        pA.append(sum(A[i:j + 1]))

for i in range(0, m - 1 + 1):
    for j in range(i + 1, m - 1 + 1):
        pB.append(sum(B[i:j + 1]))

pA.sort()
pB.sort()

ans = 0
for i in range(0, len(pA) - 1):

    target = T - pA[i]

    left = bisect_left(pB, target)
    right = bisect_right(pB, target)

    # 값이 없으면 right == left가 되어서 0이 추가됨
    ans += (right - left)

print(ans)
