'''
# comment

# https://bladejun.tistory.com/97


'''

# input 입력 받기
n = int(input())
li = sorted(map(int, input().split()))


# 이중포인터 설정
left = 0
right = n-1

answer = 2e+9 + 1  # 기준값
final = []  # 정답

# 투포인터 진행
while left < right:

    tot = li[left] + li[right]
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(tot) < answer:
        answer = abs(tot)
        final = [li[left], li[right]]

    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if tot < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    elif tot > 0:
        right -= 1
    # 합이 0이면 더 이상 볼 필요가 없음
    else:
        break


print(final[0], final[1])
