
from decimal import Decimal, getcontext
from math import sqrt

n = int(input())
a = sqrt(n)
b = n ** 0.5

c = n ** (1.0 / 3.0)  # 이 방식은 오차가 발생할 수 있음


# Demical을 이용해야 함

# https://www.acmicpc.net/source/41904955
# https://devlibrary00108.tistory.com/312

# 천자리까지 정확도 주기
getcontext().prec = 1000

N = int(input())
for _ in range(N):

    # Decimal  객체를 만듬.(float, int같은)
    # decimal 파이썬 자체 내장 함수에 대응, 500자리에서 대충 올렸다.

    d = round((int(input()) ** (Decimal('1') / Decimal('3'))), 500)

    # 원하는 소수점 자리까지 표현
    print(str(d)[0:str(d).find(".") + 11])
