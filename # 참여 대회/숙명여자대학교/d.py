import sys
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):
    n = int(input())

    a = 1
    b = 1
    temp = 1
    while True:
        b = n + 1 - temp

        if 1 <= b <= temp:
            break

        a += 1
        temp *= 2

    # (a, b)구함

    while a > 0:
        print(str(a) + "%018d" % (b))
        a -= 1
        b = (b + 1) // 2
