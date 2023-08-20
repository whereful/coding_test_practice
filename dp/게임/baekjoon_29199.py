'''
import heapq
# import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))
is_hit = [False] * n


# 두 명 공간 만들기 - 0 : 선공
score = [0] * 2
turn = 0

q = []
heapq.heapify(q)

# 최대 힙 만들기
# 점수 큰 순 : 점수가 같으면 인덱스가 큰 순
# 힙은 정렬을 보장하지 않음
for i in range(n):
    heapq.heappush(q, (-arr[i], -i))

while q:

    print(is_hit)
    print(q)
    print(score)
    print("--------------")

    # 힙에 과녁이 맞힌 게 들어 있으면 다 뺌
    # 큰 인덱스를 우선해서 -를 붙임
    if is_hit[-q[0][1]] == True:
        heapq.heappop(q)
        continue

    print(is_hit)
    print(q)
    print(score)

    # 최대값이 0보다 작으면 다음 차례는 힙에 들어있는 모든 값을 더해야 함
    if -q[0][0] < 0:
        turn = int(not turn)
        score[turn] += -sum([v for v, i in q])
        break

    data, idx = heapq.heappop(q)
    data, idx = -data, -idx

    score[turn] += data
    is_hit[idx] = True

    turn = int(not turn)

    for i in range(idx + 1, n - 1 + 1):
        if is_hit[i] == True:
            break
        score[turn] += arr[i]
        is_hit[i] = True

print(score[0])
'''

'''
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))

prefix = [arr[0]]
for i in range(1, n):
    prefix.append(prefix[i - 1] + arr[i])


dp = [0] * n
dp[0] = max(0, arr[0])

for i in range(1, n - 1 + 1):
    dp[i] = max(dp[i - 1], prefix[i] - dp[i - 1])

print(dp[n - 1])
'''

# https://www.acmicpc.net/source/65275753


n = int(input().rstrip())
scores = list(map(int, input().rstrip().split()))

dp = [-1e15 for _ in range(n + 1)]

dp[0] = (0, 0)  # me 0 enemy 0

for i, score in enumerate(scores):
    prev_best = dp[i]
    if prev_best[0] >= prev_best[1] + score:
        dp[i+1] = (prev_best[0], prev_best[1] + score)
    else:
        dp[i+1] = (prev_best[1] + score, prev_best[0])

print(dp[n][0])
