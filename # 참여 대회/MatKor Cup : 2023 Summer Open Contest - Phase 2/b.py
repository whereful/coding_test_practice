import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

sx = sum(a for a, b in arr)
sy = sum(b for a, b in arr)
sxx = sum(a ** 2 for a, b in arr)
sxy = sum(a * b for a, b in arr)

# print(n, sx, sy, sxx, sxy)

if sx ** 2 != n * sxx:
    a2 = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    b2 = (sy - a2 * sx) / n

    print(a2, b2)
    # print('%.10f %.10f' % (a2, b2))
else:
    print('EZPZ')
