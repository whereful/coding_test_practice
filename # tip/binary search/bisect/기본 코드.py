# https://heytech.tistory.com/79

from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
li = sorted(map(int, input().split()))

# m보다 크거나 같은 가장 작은 값의 인덱스
# 인덱스 범위가 배열의 범위와 일치하는지 확인
print(bisect_left(li, m))

# m보다 작거나 같은 가장 큰 값의 인덱스
# 인덱스 범위가 배열의 범위와 일치하는지 확인
print(bisect_right(li, m) - 1)

# a이상 b이하의 정수 개수
a, b = map(int, input().split())

print(bisect_right(li, b) - bisect_left(li, a))
