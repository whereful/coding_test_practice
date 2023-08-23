# https://www.acmicpc.net/source/61471402

from decimal import *

# 1000자리까지 정확하게 계산
getcontext().prec = 1000

a = 0.1
b = 0.2

print(a + b, type(a + b))

# 문자열 입력하지 않으면 정확하지 않음
c = Decimal("0.1")
d = Decimal("0.2")

print(c + d, type(c + d))

# Decimal끼리 계산하고 round(N, 넉넉한 자리수)을 적용해야 정확한 결과를 얻을 수 있음
# 이유는 모름
e = round(c + d, 300)
