n = int(input())
print(' '.join(map(str, [2] + [4 * i for i in range(1, n - 1 + 1)])))
