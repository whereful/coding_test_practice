# 가로 뒤집기

'''
가로 뒤집기
a[0][1] a[0][0]
a[1][1] a[1][0]
a[2][1] a[2][0]
'''

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a = [l[::-1] for l in a]


# 세로 뒤집기 = 배열 전체 | 회전 | 시계방향 90도 * 2번 + 가로 뒤집기

'''
세로 뒤집기
a[2][0] a[2][1]
a[1][0] a[1][1]
a[0][0] a[0][1]
'''

for _ in range(2):
    a = list(zip(*a[::-1]))

a = [l[::-1] for l in a]
