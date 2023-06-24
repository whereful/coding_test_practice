'''
# comment

1. r == 0 이면 n의 모든 약수의 합 // n이 대상
2. r > 0 이면 m > r, (n-r) % m을 만족하는 m의 총합 // n-r이 대상

'''

from math import sqrt

n, r = map(int, input().split())

s = 0

# 나머지가 0이면 n의 약수의 총합을 구하면 된다
if r == 0:

    # 약수들을 저장하는 집합을 선언
    divisor_set = set()

    # a * b == n을 만족하는 a, b를 집합에 추가한다
    for a in range(1, int(sqrt(n)) + 1):
        if n % a == 0:
            divisor_set.add(a)
            divisor_set.add(n // a)

    s = sum(divisor_set)

# 나머지가 0보다 크면 n - r의 약수들을 살펴본다
else:

    # 약수들을 저장하는 집합을 선언
    divisor_set = set()

    # a * b == n - r을 만족하는 a, b를 구한다
    for a in range(1, int(sqrt(n - r)) + 1):
        if (n - r) % a == 0:
            # a, b들 중에서 r보다 크고 n의 약수가 아닌 것만 집합에 추가한다
            b = (n - r) // a

            if a > r:
                divisor_set.add(a)
            if b > r:
                divisor_set.add(b)

    s = sum(divisor_set)

print(s)
