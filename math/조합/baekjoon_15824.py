'''
[2, 5, 8]에서 가능한 모든 조합의 최대 - 최소는

(2, 5), (5, 8), (2, 8), (2, 5, 8)로 4개 씩 따로 계산하면 좋지 않다


# 2가 최대인 조합의 개수 + 5가 최대인 조합 개수 + 8이 최대인 조합 개수 - 2가 최소인 조합의 개수 - 5가 최소인 조합의 개수 - 8이 최소인 조합의 개수

이렇게 계산해야 효율적(전체를 봐야 한다)


2가 최대인 조합의 개수 : 2**0개, 2가 최소인 조합의 개수 : [5, 8]로 만들 수 있는 조합의 개수이므로 2 ** (n - 1 - i)개 // i = 0

'''

# https://0902.tistory.com/60
# https://mangu.tistory.com/170?category=937146
# https://mingchin.tistory.com/429?category=987465

import sys
def input(): return sys.stdin.readline().strip()


mod = int(1e9 + 7)

n = int(input())
arr = sorted(map(int, input().split()))

ans = 0
for i in range(n):
    ans = (ans % mod + (pow(2, i, mod) - pow(2, n - i - 1, mod)) %
           mod * arr[i] % mod) % mod
print(ans % mod)
