from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()


n, m, k = map(int, input().split())

# 데미지를 많이 입히는 캐릭터를 뽑는 것이 좋음
character = sorted([int(input()) for _ in range(n)], reverse=True)[:m]

boss = [list(map(int, input().split())) for _ in range(k)]

idx_list = [i for i in range(k)]
all_p = []
for i in range(0, k + 1):
    all_p += list(combinations(idx_list, i))

# print(character, boss, all_p)

ans = 0

# 캐릭터를 일일이 살핌
for c in character:

    part = 0
    # 쓰러뜨릴 보스를 선택함
    for p in all_p:

        weight = 0
        value = 0

        # 각 보스에 대해서 더함
        for i in p:
            # print(c, p, i, boss[i][0], boss[i][1])

            # 가능한 데미지 양은 c에 대한 올림으로 처리
            weight += ((boss[i][0] - 1) // c + 1) * c
            value += boss[i][1]

        # 총 가능한 양보다 작은 경우도 성립함
        if 900 * c >= weight:
            # print(c, 900 * c, weight)
            part = max(part, value)

    ans += part

print(ans)
