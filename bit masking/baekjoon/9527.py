# https://blog.naver.com/dsyun96/221843554389

from math import log2


def f(n):
    if n <= 0:
        return 0

    k = int(log2(n))

    res = 0
    for i in range(0, k + 1):
        l = (n + 1) // pow(2, i + 1) * pow(2, i)
        r = max(0, (n + 1) % pow(2, i + 1) - pow(2, i))
        res += (l + r)

    return res


a, b = map(int, input().split())

print(f(b) - f(a - 1))
