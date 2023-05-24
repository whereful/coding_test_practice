'''
# comment

# https://hongcoding.tistory.com/14

# https://heytech.tistory.com/79

'''


# stack은 정렬되게 삽입됨
def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if stack[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


n = int(input())
li = list(map(int, input().split()))

stack = [0]


for l in li:
    # 수열의 최대값이 l보다 작으면 수열에 추가
    if stack[-1] < l:
        stack.append(l)
    #
    else:
        stack[binary_search(l, 0, len(stack) - 1)] = l

# 0이 들어 있어서 0을 제외해야 함
print(len(stack) - 1)
