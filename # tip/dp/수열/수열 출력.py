n = int(input())
li = list(map(int, input().split()))

# dp 적용 함수


def f(li):
    return []


# dp가 완성되었다고 가정
dp = f(li)

ans = []
idx = max(dp)

# dp 조건을 만족하는 여러 수열 중 무작위로 출력하게 됨
for i in range(n - 1, 0 - 1, -1):
    if dp[i] == idx:
        ans.append(li[i])
        idx -= 1

print(*reversed(ans))
