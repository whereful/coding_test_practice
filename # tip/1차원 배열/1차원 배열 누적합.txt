'''
해당 문제

백준
2143

'''

# prefix에 누적합의 모든 경우를 저장하는 경우
li = list(map(int, input().split()))
n = len(li)

prefix = []
for i in range(0, n - 1 +1):
    for j in range(i, n - 1 +1):
        prefix.append(sum(li[i:j +1]))


# prefix에 시작점이 0으로 고정된 누적합만 저장하는 경우

# 시작점이 0인 경우만 배열에 저장되어서 구간합을 구하려면 함수를 적용해야 함
def prefix_sum(a, b):
    if a == 0:
        return prefix[b]
    return prefix[b] - prefix[a - 1]

li = list(map(int, input().split()))
n = len(li)

prefix = []
for i in range(0, 1 - 1 +1): # 시작점을 0만 조회하도록 설정하면 된다
    for j in range(i, n - 1 +1):
        prefix.append(sum(li[i:j +1]))