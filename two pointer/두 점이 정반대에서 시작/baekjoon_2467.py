'''
# comment

# https://bladejun.tistory.com/97


'''


def two_pointer():

    left = 0
    right = n-1

    answer = 3e+9  # 기준값
    a = b = 0

    # 투포인터 진행
    while left < right:

        tot = li[left] + li[right]
        # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
        if answer > abs(tot):
            answer = abs(tot)
            a = li[left]
            b = li[right]

        # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
        if tot < 0:
            left += 1
        # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
        elif tot > 0:
            right -= 1
        # 두 용액의 합이 0인 경우를 명시하지 않으면 무한 순회 반복됨
        else:
            break

    print(a, b)


n = int(input())
li = sorted(map(int, input().split()))

two_pointer()
