'''

from math import sqrt
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
A = list(map(int, input().split()))
A = set(A)

q = int(input())
L = list(map(int, input().split()))

# dp : 1 -> 100000으로 진행되는 모든 경우의 수
dp = [1] * (100000 + 1)

for i in range(4, 100000 + 1):
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0 and j != i // j:
            dp[i] += (dp[j] + dp[i // j])
        elif i % j == 0 and j == i // j:
            dp[i] += dp[j]

answer = []
for l in L:
    count = 0
    for s in range(1, int(sqrt(l)) + 1):
        if l % s == 0 and s != l // s:

            if s in A:
                count += dp[l // s]
            if l // s in A:
                count += dp[s]

        elif l % s == 0 and s == l // s:
            if s in A:
                count += dp[s]

    answer.append(count)

print(' '.join(map(str, answer)))

'''

# https://www.acmicpc.net/source/64646283

# https://www.acmicpc.net/source/64686666

n = int(input())
A = [*map(int, input().split())]
q = int(input())
L = [*map(int, input().split())]

# x[i] : 길이 i를 만들 수 있는 총 경우의 수(시작점은 상관 없음) // ? -> a

# 예를 들어 4인 경우에는 ? -> 1 -> 4, ? -> 2 -> 4 두 가지 방법이 있음 ==> 따라서 ? -> 4는 ? -> 2 + ? -> 1을 더한 것과 같음

# 그리고 a에 대해서만 1로 정의하는 거는 존재하지 않는 시작 막대에 대해서는 만들 수 있는 방법이 없기 때문임
# x는 0부터 100000까지의 막대를 만들 수 있는 모든 경우의 수를 정의함
X = [0] * (100000 + 1)
for a in A:
    X[a] = 1
for i in range(1, 100001):
    for j in range(i+i, 100001, i):
        X[j] += X[i]

# 그 중에서 내가 확인하고 싶은 거는 l에 관한 것 - 그래서 x[l]을 출력하는 것임
# x[l]을 문자열로 만들어 출력
print(' '.join(map(lambda x: str(X[x]), L)))
