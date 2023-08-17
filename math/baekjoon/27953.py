d1, d2, x = map(int, input().split())
d1, d2 = max(d1, d2), min(d1, d2)


print(d1 * d2 * 100 / (d2 * x + d1 * (100 - x)))
