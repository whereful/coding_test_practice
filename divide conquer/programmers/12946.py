# 분할 정복

def solution(n):

    def f(n, a, b, c):
        if n == 2:
            return [[a, b], [a, c], [b, c]]
        return f(n - 1, a, c, b) + [[a, c]] + f(n - 1, b, a, c)

    return f(n, 1, 2, 3)
