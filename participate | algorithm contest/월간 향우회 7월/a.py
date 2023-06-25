'''
# comment

정렬의 성질
- 정렬을 하여도 for i in range(0, n - 1 +1): for j in range(i + 1, n - 1 +1): mem(arr[i], arr[j])의 결과는 변하지 않는다

1보다 큰 모든 수 : a

mem(0, 0) = 1
mem(0, 1) = 2
mem(0, a) = 1

mem(1, 1) = 0
mem(1, a) = 0
mem(a, a) = 0

0인 경우에 대해서만 고려하면 된다

'''


n = int(input())

# 정렬 가능
arr = sorted(map(int, input().split()))

count_0 = arr.count(0)
count_1 = arr.count(1)
count_a = n - count_0 - count_1

s = 0
for i in range(count_0):
    s += (i + 2 * count_1 + count_a)

print(s)
