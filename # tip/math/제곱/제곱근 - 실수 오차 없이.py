from decimal import *
from math import sqrt

n = int(input())
a = sqrt(n)
b = n ** 0.5

# c = n ** (1.0 / 3.0)  # 이 방식은 오차가 발생할 수 있음
# print(c)


# Demical을 이용해야 함

# https://www.acmicpc.net/source/41904955
# https://devlibrary00108.tistory.com/312

getcontext().prec = 400  # 천자리까지 정확도 주기

for i in range(int(input())):

    # Decimal을 이용하여 계산
    res = Decimal(str(Decimal(input()) ** (Decimal('1.0') / Decimal('3.0'))))

    # 이 과정이 왜 필요한지는 모르겠으나 정확성을 부여하기 위해 실행
    # 반올림하는 자리수는 prec보다 작아야 오류가 발생하지 않음
    res = round(res, 300)

    # 원하는 자리수만큼 0.0000000001을 채우고 내림처리
    print(res.quantize(Decimal('0.0000000001'), rounding=ROUND_DOWN))
