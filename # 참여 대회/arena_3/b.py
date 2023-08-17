from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())

if int(sqrt(n)) == sqrt(n):
    print(-1)
    exit(0)

ans = 0
for i in range(1, int(sqrt(n)) + 1):
    k = n - i ** 2

    # k의 제곱근이 정수이면
    if int(sqrt(k)) == sqrt(k):
        ans += 1

# 쌍이 중복되면 중복된 것 제거
ans = (ans + 1) // 2

# 1 ** 2, 2 ** 2, 3 ** 2, ... k ** 2에서 제곱 사이의 차이는 3, 5, 7, ... 홀수
# 그러면 제곱과 제곱의 차이는 (3 + 5 + 7 + ...), (7 + 9 + ... )으로 나타낼 수 있다
# (3 + 5 + ... 2a + 1), (5 + 7 + ... 2a + 1)는 a(a + 2), a(a + 4)등으로 차이가 짝수이다
# 따리서 a(a+2b) = n이려면 약수 쌍의 차이가 짝수여야 한다
for i in range(1, int(sqrt(n)) + 1):
    # i가 n의 약수이고 쌍의 차가 짝수이면
    if n % i == 0 and ((n // i) - i) % 2 == 0:
        ans += 1

print(ans)
