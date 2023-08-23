from decimal import *
getcontext().prec = 400

'''
# https://wikidocs.net/21113

# https://puleugo.tistory.com/43

# ceil, floor은 정수만 도출
# round는 반올림하면 오류 발생
'''

# https://m.blog.naver.com/youndok/222218536425
# https://brightnightsky77.tistory.com/201
# https://ko.from-locals.com/python-round-decimal-quantize/

# S : Decimal을 이용하여 계산한 값, round처리를 해서 오류 처리 및 0 채우기
S = Decimal('0.1') + Decimal('0.2')

N = round(S, 300)

# A번째자리까지 반올림
N.quantize(Decimal('0.0000000001'), rounding=ROUND_HALF_UP)

# A번째자리까지 올림
N.quantize(Decimal('0.0000000001'), rounding=ROUND_UP)

# A번째자리까지 내림
N.quantize(Decimal('0.0000000001'), rounding=ROUND_DOWN)
