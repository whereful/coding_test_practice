a = int(input())  # a >= 1
b = 0

# https://yiyj1030.tistory.com/149
# x ^ x = 0이 항상 성립
# b ^ a = a // 0을 xor연산해도 그대로 유지된다

# https://jeonggyun.tistory.com/208

# https://sdev.tistory.com/50


'''
# https://gukin.tistory.com/14

# https://velog.io/@studyhard/ps-boj-2830

비트 연산은 묶어서 계산하지 않고 나누어서 계산하는 것이 편하다

예를 들어
011 ^ 111 + 001 ^ 101을 계산하려면

두 값을 계산해서 더하는 것이 아니라

2**2의 자리수 : 0 ^ 1, 0 ^ 1 존재
2**1의 자리수 : 1 ^ 1, 0 ^ 0 존재
2**0의 자리수 : 1 ^ 1, 1 ^ 1 존재

각 자리수에 존재하는 묶음들의 합을 계산하면 됨

'''
