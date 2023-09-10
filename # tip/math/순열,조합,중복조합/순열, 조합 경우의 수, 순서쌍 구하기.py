from itertools import permutations, combinations

n, r = map(int, input().split())
a = list(permutations([i for i in range(1, n + 1)], r))
b = list(combinations([i for i in range(1, n + 1)], r))

print(a, len(a))
print(b, len(b))
