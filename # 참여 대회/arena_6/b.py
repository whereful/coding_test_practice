'''
a초에 arba 적용

몬스터 : a + 90 미만까지 통하지 않음
사람 : a + 100까지 사용할 수 없음

스킬을 사용할 수 있는 시점, 몬스터에게 적용할 수 있는 시점이 다름


90 < 100, 360이어서 대기 시간만 고려하면 됨

'''

n, m = map(int, input().split())
arba = sorted(list(map(int, input().split())))
origin = sorted(list(map(int, input().split())))

stack_a = [arba[0]]
res_a = 1
for i in range(1, len(arba) - 1 + 1):
    if arba[i] - stack_a[-1] >= 100:
        stack_a.append(arba[i])
        res_a += 1

stack_b = [origin[0]]
res_b = 1
for i in range(1, len(origin) - 1 + 1):

    # origin[i + 1] - origin[i] >= 360으로 하지 않은 이유는 0 10 360의 경우 개수가 2인데 사이의 차이가 둘 다 360보다 작아서 개수가 1이 나오기 때문
    if origin[i] - stack_b[-1] >= 360:
        stack_b.append(origin[i])
        res_b += 1

print(res_a, res_b)
