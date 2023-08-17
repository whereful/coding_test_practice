'''
해당 문제

백준
27172

'''


# 1. 기본 코드

from math import sqrt

n = int(input())

array = [True] * (n + 1)
array[0] = array[1] = False

for i in range(2, int(sqrt(n)) + 1):

    # if array[i] == True:
    #     multiple = 2

    #     while multiple * i <= n:
    #         array[multiple * i] = False
    #         multiple += 1

    if array[i] == True:
        for j in range(i * 2, n + 1, i):
            array[j] = False


# 2. 시간복잡도 : https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity / 사실상 O(n)

# 3. 응용 - 에라토스테네스의 체의 기본 원리 자체는 소수 판별뿐만 아니라 약수에서도 특정 수의 약수인지를 판별할 때도 사용 가능하다
