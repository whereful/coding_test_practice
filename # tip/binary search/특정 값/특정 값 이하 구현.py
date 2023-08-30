# X : 조건 만족하지 않음, O 조건 만족
# O O O O O X X X X X ...

# 해당 인덱스 전 : 특정 값 미만
# 해당 인덱스 후 : 특정 값 이상

# 이 때는 특정 값보다 같거나 이하이지만 가장 큰 값의 인덱스를 구함
# O O O O [O] X X X X X ...

'''
해당 문제

백준
2512
28140

'''


# li는 정렬되어 있다고 가정
# 따라서 li의 구간도 정렬되어 있어 binary search 적용 가능

# bisect_right(배열, 찾는 값) - 1과 동일

# 구현
def binary_search(start, end):

    # result를 아무 값으로 설정
    result = 0

    while start <= end:
        mid = (start + end) // 2

        # 조건을 설정할 때 필요한 값 정의

        # 특정 값보다 이하인 경우(조건 만족)
        # target은 기준점
        if target >= ():
            result = mid
            start = mid + 1
        # 특정 값보다 초과인 경우(조건 불만족)
        else:
            end = mid - 1

    # 최종 결과를 반환함
    return result


li = sorted(map(int, input().split()))
target = int(input())

n = len(li)
print(binary_search(0, n - 1))
