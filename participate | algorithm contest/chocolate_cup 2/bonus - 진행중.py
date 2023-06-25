'''
# comment

에라토스테네스의 체

매우 큰 소수 구하기
'''

from math import sqrt

is_prime_list = [True] * (100000000 + 1)
is_prime_list[0] = is_prime_list[1] = False

for i in range(2, int(sqrt(100000000)) + 1):
    multiple = 2
    if is_prime_list[i] == True:
        while multiple * i <= 100000000:
            is_prime_list[multiple * i] = False
            multiple += 1

prime = [i for i in range(10000000, 100000000 + 1) if is_prime_list[i] == True]

for i in range(11):
    print(prime[i], end=' ')
