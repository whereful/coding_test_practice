from math import sqrt

# i * i == n인 경우 방지
divisor_set = set()

# a * b == n을 만족하는 a, b를 저장하는 수들을 집합에 저장
# b == n // a

# 약수 == 배수로 전환 가능

n = int(input())
for a in range(1, int(sqrt(n)) + 1):
    if n % a == 0:
        divisor_set.add(a)
        divisor_set.add(n // a)
