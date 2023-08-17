'''
# comment

# baekjoon_2467과 유형 동일
'''

# 문제의 특별한 매개변수 part, li


def two_pointer(part, li):

    left = 0
    right = len(li) - 1

    answer = 3e+10  # 기준값

    # 세 용액이어서 변수 추가
    a = b = c = 0

    # 투포인터 진행
    while left < right:

        # 세 수의 합이 0에 가까워야 함
        tot = li[left] + li[right] + part

        # 세 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
        if answer > abs(tot):
            answer = abs(tot)
            a = li[left]
            b = li[right]

            c = part

        # 세 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
        if tot < 0:
            left += 1
        # 반대로, 세 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
        elif tot > 0:
            right -= 1
        # 세 용액의 합이 0인 경우를 명시하지 않으면 무한 순회 반복됨
        else:
            break

    return sorted([a, b, c])


n = int(input())

# 기준이 되는 배열이 아님
arr = sorted(map(int, input().split()))

# 정답 배열 선언
ans = [3e11, 3e11, 3e11]

for i in range(0, n - 1 + 1):

    # 기준이 되는 배열 li, 기존 인덱스 i를 제거
    li = arr[:]
    li.pop(i)

    part = arr[i]

    candidiates = two_pointer(part, li)

    if abs(sum(candidiates)) < abs(sum(ans)):
        ans = candidiates

print(*ans)
