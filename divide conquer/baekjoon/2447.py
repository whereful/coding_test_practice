'''
# comment

출력물을 배열로 보는 관점

# https://www.acmicpc.net/source/58512766

공식으로 작성
'''

'''
def DC_final(sy, sx):
    for i in range(0, 2 + 1):
        for j in range(0, 2 + 1):
            if i == 1 and j == 1:
                continue
            else:
                arr[i + sy][j + sx] = '*'


def DC(l, sy, sx):
    if l == 3:
        DC_final(sy, sx)
        return

    T = l // 3

    for i in range(0, 2 + 1):
        for j in range(0, 2 + 1):
            if i == 1 and j == 1:
                continue
            else:
                DC(T, i * T + sy, j * T + sx)


n = int(input())

arr = [[' '] * n for _ in range(n)]

DC(n, 0, 0)

for a in arr:
    print(''.join(a))
'''


def divide(n):
    if n == 3:
        return ['***', '* *', '***']

    pd = divide(n // 3)
    stars = []

    for p in pd:
        stars.append(p * 3)
    for p in pd:
        stars.append(p + ' ' * (n // 3) + p)
    for p in pd:
        stars.append(p * 3)

    return stars


n = int(input())

print('\n'.join(divide(n)))
