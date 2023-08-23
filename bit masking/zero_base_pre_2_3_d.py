'''
문제

숫자 a, b를 이진수로 바꾸었을 때 서로 다른 부분의 개수


'''


def solution(A, B):
    # xor 연산 값에서 1(다르면 1이 도출) 개수를 세면 됨
    return bin(A ^ B)[2:].count('1')
