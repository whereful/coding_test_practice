'''
# 행, 열 길이 다름

# 삼각형을 채우는 게 아니라 삼각형을 둘러싼 사각형을 채우는 방식

# 공식으로 작성

# https://www.acmicpc.net/source/54390698
간단한 공식으로 적용 가능

'''

'''
def DC_final(sy, sx):
    # 배열의 일부분을 다른 배열로 대체
    arr[0 + sy][sx:sx + 4 + 1] = [' ', ' ', '*', ' ', ' ']
    arr[1 + sy][sx:sx + 4 + 1] = [' ', '*', ' ', '*', ' ']
    arr[2 + sy][sx:sx + 4 + 1] = ['*', '*', '*', '*', '*']

# c == r * 2 - 1


def DC(r, c, sy, sx):
    if r == 3:
        DC_final(sy, sx)
        return

    T = r // 2
    DC(T, T * 2 - 1, sy, T + sx)
    DC(T, T * 2 - 1, T + sy, sx)
    DC(T, T * 2 - 1, T + sy, T * 2 + sx)


n = int(input())
r = n
c = r * 2 - 1

arr = [[' '] * (n * 2 - 1) for _ in range(n)]

DC(n, n * 2 - 1, 0, 0)

for a in arr:
    print(''.join(a))
'''


def divide(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    pd = divide(n // 2)
    stars = []

    for p in pd:
        stars.append(' ' * (n // 2) + p + ' ' * (n // 2))
    for p in pd:
        stars.append(p + ' ' + p)

    return stars


n = int(input())

print('\n'.join(divide(n)))
