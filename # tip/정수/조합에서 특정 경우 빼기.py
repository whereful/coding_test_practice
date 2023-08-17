from itertools import combinations

# [0,1,2,3,4,5] 중에서 (0, 5), (1, 4), (2, 3)처럼 합이 5인 것이 포함된 것을 빼고 싶다

a = list((a, b, c) for a, b, c in combinations(
    [0, 1, 2, 3, 4, 5], 3) if a + b != 5 and a + c != 5 and b + c != 5)
