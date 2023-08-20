a = [[i * j for i in range(1, 5)] for j in range(1, 5)]


print(a)
# 2차원 배열 전체 최솟값
print(min(map(min, a)))
