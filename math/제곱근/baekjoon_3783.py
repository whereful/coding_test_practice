# Demical을 이용해야 함

# https://www.acmicpc.net/source/41904955
# https://devlibrary00108.tistory.com/312

from decimal import Decimal, getcontext
getcontext().prec = 1000  # 천자리까지 정확도 주기

for _ in range(int(input())):

    # Decimal 객체를 만듬.(float, int같은)
    # decimal을 이용해서 정확한 세제곱근 구함, 구한 값을 500자리에서 반올림 실행
    # 500 자리에서 실행한 이유는 여유있게 소수점을 만들기 위함

    d = round((int(input()) ** (Decimal('1') / Decimal('3'))), 500)

    # 원하는 소수점 자리까지 표현
    print(str(d)[0:str(d).find(".") + 11])
