'''
# comment

# baekjoon_12015와 원리 동일하지만 실제 수열을 구하기 위한 배열 추가

# https://hongcoding.tistory.com/14
# 길이만 구할 수 있다

# # https://heytech.tistory.com/79

# https://www.acmicpc.net/board/view/110831
# 반례 - 1 3 4 5 2 4에서 가장 긴 수열은 1 3 4 5이지만 1 2 4 5가 저장되는 문제가 발생
# 맨 마지막 원소만 변경할 경우 10 14 7 8 9처럼 시작점을 바꿔야 하는 경우 반영하지 못하는 문제 발생

# https://rebro.kr/33

# https://velog.io/@veonico/%EB%B0%B1%EC%A4%80-14003.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-5-python%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''


def binary_search(start, end):

    # 최종 인덱스를 저장하는 변수
    result = 0

    while (start <= end):
        mid = (start + end) // 2

        # 특정값 이상이면
        # 최종 변수에 저장 및 범위 축소
        if a <= li[mid]:
            result = mid
            end = mid - 1
        # 특정값 미만이면 범위 확장
        else:
            start = mid + 1

    return result


def return_real_li(temp_li, n):

    real_li = []

    while temp_li and n:

        num, idx = temp_li.pop()

        if idx == n:

            real_li.append(num)
            n -= 1

    # 크기가 큰 순서대로 삽입되어서 뒤집어야 함
    return real_li[::-1]


n = int(input())

arr = list(map(int, input().split()))

li = [-1e11]

# 실제 수열을 구하기 위한 배열 설정
# li가 실제 수열을 구할 수 없음
# 0은 -1e11이 li에 삽입된 인덱스 위치
temp_li = [(-1e11, 0)]

for a in arr:

    if a > li[-1]:
        # ex) -1e11 다음에 2가 삽입됨
        # li에는 [-1e11, 2]로 설정됨
        # 2가 삽입된 위치는 기존 [-1e11] 배열의 길이
        # 따라서 real_li를 먼저 설정해야 함
        temp_li.append((a, len(li)))

        li.append(a)

    else:
        index = binary_search(0, len(li) - 1)
        li[index] = a

        # a가 삽입되는 위치는 index이므로 real_li에 반영
        temp_li.append((a, index))

# 맨 앞의 원소는 길이 측정에서 제외해야 함
print(len(li) - 1)
# 수열 전체 출력
print(*return_real_li(temp_li, len(li) - 1))
