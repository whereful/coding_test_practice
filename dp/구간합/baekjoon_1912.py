# https://www.youtube.com/watch?v=WpH0_YzjX78

n = int(input())
li = list(map(int, input().split()))

cur_sum, max_sum = 0, li[0]

for i in range(0, n - 1 + 1):
    cur_sum = max(cur_sum + li[i], li[i])
    max_sum = max(cur_sum, max_sum)

print(max_sum)
