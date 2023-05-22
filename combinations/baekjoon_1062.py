'''
# comment

# combinations
'''

from itertools import combinations

n, k = map(int, input().split())

# a, n, t, i, c를 제외한 전체 알파벳
all = 'bdefghjklmopqrsuvwxyz'

# 중복을 제거한 집합(antic)는 무조건 배워야 하므로 제외
li = [set(input()) - set('antic') for _ in range(n)]

# antic 길이보다 작으면 바로 종료
if k < 5:
    print(0)
    exit(0)

# k-5(antic 제외)로 만들 수 있는 모든 알파벳 조합 형성
chars = [set(l) for l in list(combinations(all, k - 5))]

ans = 0

# 조합들 중에서 부분 집합을 포함하는 최대 조합이 갖는 길이 찾기
for c in chars:
    # 집합에서 >=는 부분 집합을 의미
    ans = max(ans, sum([c >= l for l in li]))

print(ans)
