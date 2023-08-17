'''
# comment

# two pointer : left = right = 0

# prefix sum
'''


def prefix_sum(left, right):
    if left <= 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


def two_pointer():
    left = right = 0

    length = n

    # 문제의 특별한 변수
    flag = 0

    while left <= right and right <= n - 1:

        interval = prefix_sum(left, right)

        # print(interval, left, right)

        if interval < s:
            right += 1
        else:
            length = min(length, right - left + 1)
            left += 1

            # 문제의 특별한 코드
            flag = 1

    # 문제의 특별한 코드
    print(length if flag == 1 else 0)


n, s = map(int, input().split())

li = list(map(int, input().split()))

prefix = []
sum = 0
for i in range(n):
    sum += li[i]
    prefix.append(sum)

# print(prefix)

two_pointer()
