'''
# comment

# https://hongcoding.tistory.com/14
# 길이만 구할 수 있다

# https://heytech.tistory.com/79

# https://www.acmicpc.net/board/view/110831
# 반례 - 1 3 4 5 2 4에서 가장 긴 수열은 1 3 4 5이지만 1 2 4 5가 저장되는 문제가 발생

# https://rebro.kr/33

# https://velog.io/@veonico/%EB%B0%B1%EC%A4%80-14003.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-5-python%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''


def binary_search(start, end):

    # result를 아무 값으로 정의
    result = 0
    while start <= end:

        mid = (start + end) // 2

        # li의 값이 특정 값 이상인 경우 범위 축소
        # target <= ()
        if a <= li[mid]:
            result = mid
            end = mid - 1
        # li의 값이 특정 값 미만인 경우 범위 확장
        else:
            start = mid + 1

    return result


n = int(input())

# 정렬하지 않은 배열 입력받음
arr = list(map(int, input().split()))

# 문제에서 정렬된 배열을 설정함
li = [0]


# 정렬되지 않은 배열 순차 탐색
for a in arr:

    # 정렬된 배열의 가장 큰 값이 원소보다 작으면 정렬된 배열 뒤에 원소 추가
    if a > li[-1]:
        li.append(a)

    # 정렬된 배열의 가장 큰 값이 원소보다 크거나 같은 경우
    # ex) 10 20 40 45에서 39를 탐색
    # 40을 39로 바꾸어야 함
    # X X X X [O] O O ...
    # X : a > li[i], O : a <= li[i]
    # a 이상인 값 중 가장 작은 값의 인덱스를 구해야 함
    # 특정 값 이상인 경우의 binary_search 적용
    else:
        li[binary_search(0, len(li) - 1)] = a

# 0이 들어 있어서 0을 제외해야 함
print(len(li) - 1)
