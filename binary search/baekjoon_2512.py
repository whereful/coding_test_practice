'''
# comment

# arr[-1] 대신 100000을 대입하였을 때 오류 발생

# 반례
5
70 80 30 40 100
450

70 + 80 + 30 + 40 + 100 = 320

모든 경우에 대하여 만족(O O O O .... )

따라서 문제에서 제시된 배열의 최댓값까지 탐색해야 함

'''


def binary_search(start, end):

    # result를 아무 값으로 정의
    result = 0

    while (start <= end):
        mid = (start + end) // 2

        # 후보값 구함
        can = sum([min(li[mid], a) for a in arr])

        # 특정값 이하인 경우
        # target >= ()
        if m >= can:
            result = mid
            start = mid + 1

        # 특정값을 초과한 경우
        else:
            end = mid - 1

    return result


n = int(input())

# 정렬되지 않은 배열을 입력받음
arr = sorted(map(int, input().split()))
m = int(input())

# 정렬된 배열을 문제에서 추출함
li = [i for i in range(1, arr[-1] + 1)]

ans = binary_search(0, len(li) - 1)
print(li[ans])
