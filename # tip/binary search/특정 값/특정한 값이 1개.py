# 찾는 원소가 1개만 존재하는 경우
# bisect_left(배열, 찾는 값), bisect_right(배열, 찾는 값)과 동일


# start, end는 배열의 처음과 끝 인덱스를 저장
def binary_search(start, end):

    while start <= end:
        mid = (start + end) // 2

        # 조건을 설정할 때 필요한 값 정의

        # 특정 값보다 작은 경우
        # 최소 지점을 높임
        if ():
            start = mid + 1

        # 특정 값보다 큰 경우
        # 최대 지점을 낮춤
        elif ():
            end = mid - 1

        # 조건을 만족했으면 더 이상 볼 필요가 없음
        else:
            return mid

    # 찾지 못하면 존재할 수 없는 인덱스 반환
    return -1


li = sorted(map(int, input().split()))
n = len(li)

print(binary_search(0, n - 1))
