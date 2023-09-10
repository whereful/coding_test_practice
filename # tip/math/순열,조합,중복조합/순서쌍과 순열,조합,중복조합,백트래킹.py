'''
(1,2,3,4,5,6,7,8,9,10)

(a,b,c,d,e)에 대응시키는 경우 : 순열 -> 10P5

(1,2,3,4,5,6,7,8,9,10)

(a,a,b,b,b,c,c,c)에 대응시키는 경우 : 조합 -> 10C2 * 8C3 * 5C3

--------------------
# https://mathjk.tistory.com/3132
# https://hsm-edu-math.tistory.com/583

a + b + c = 10

0 <= a <= 3, 0 <= b <= 4, 0 <= c <= 5일 때 모든 경우의 수를 구하는 경우

3H10 - (a가 4인 경우 -> a + b + c = 6, b가 5인 경우 ~)

--------------------

a + b + c = 10

0 <= a <= 3, 0 <= b <= 4, 0 <= c <= 5일 때 모든 순서쌍을 구하는 경우

-> 백트래킹


'''


def dfs(s, depth, li):
    # print(s, depth, li)
    if depth == len(class_list) - 1:

        # 합이 조건에 일치하는 경우
        if s == n:
            ans.append(li)

        return

    for i in range(class_list[depth + 1] + 1):

        # 안 되는 경우 미리 구분
        if s + i > n:
            continue
        dfs(s + i, depth + 1, li + [i])


# [3, 4, 5]
class_list = list(map(int, input().split()))

# 10
n = int(input())

ans = []

for i in range(class_list[0] + 1):
    # 0 ~ li[0]까지 범위의 i, 인덱스 0 선택, i일 때 경우를 담은 리스트
    dfs(i, 0, [i])

print(ans)
