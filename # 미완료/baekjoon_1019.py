# https://www.acmicpc.net/source/6082159

a = [0] * 10
s = input()
n = int(s)
f = 1

# 자리수만큼 반복
for _ in s:
    v = f * 10

    # 0 ~ 9까지 반복
    for i in range(10):
        a[i] += (n // v - (i < 1)) * f + min(max(n % v + 1 - i * f, 0), f)
    f = v
print(*a)
