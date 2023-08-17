# https://nukoori.tistory.com/40#%EC%BD%94%EB%93%9C(%20python%20)-1

'''
import sys
def input(): return sys.stdin.readline().strip()


T = 1000000007


def f(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a % T
    elif b % 2 == 1:
        return (a % T * f(a, b - 1)) % T

    temp = f(a, b // 2)
    return (temp * temp) % T


N, M, A = map(int, input().split())
H = int(input())

print(f(M, N - 1))
'''

n, m, a = map(int, input().split())
print(pow(m, n - 1, 1000000007))
