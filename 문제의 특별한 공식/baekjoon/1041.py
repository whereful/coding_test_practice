# 두 면인 경우, 3면인 경우 다 고려해야 함
# 주사위 합 면의 공식 추출해야 함

# 첫 번째 경우를 항상 조심해야 함

from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

# f : 면의 개수만큼의 합
f_1 = min(arr)

f_2 = min([arr[a] + arr[b] for a, b in combinations([0, 1, 2, 3, 4, 5], 2)
           if a + b != 5])

f_3 = min([arr[a] + arr[b] + arr[c] for a, b, c in combinations(
    [0, 1, 2, 3, 4, 5], 3) if a + b != 5 and a + c != 5 and b + c != 5])

# else 뒤 조심
print((n - 2) * (5 * n - 6) * f_1 + (8 * n - 12)
      * f_2 + 4 * f_3 if n >= 2 else sum(arr) - max(arr))
