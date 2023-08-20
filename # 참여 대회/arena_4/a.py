k = float(input())

a = k * pow(10, 9)

if int(a) != a:
    print('NO')
else:
    print('YES')
    print(int(a), pow(10, 9))
