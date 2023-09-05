'''
# https://salon.tistory.com/11
# https://www.acmicpc.net/submit/2003/65723403
# https://www.acmicpc.net/board/view/56921

반례

3 1
1 2 1

left += 1을 하였을 때 중간에 left > right가 되어서 모든 배열을 살피지 않고 반복문을 탈출하는 오류 발생

while문으로 left, right를 살피는 방식은 적절하지 않음
'''

# https://oranz.tistory.com/41

n, s = map(int, input().split())
arr = list(map(int, input().split()))


temp = 0  # 합을 저장하는 공간 temp

start = 0  # 왼쪽 포인터 start

ans = 0  # 개수 저장 ans

for i in range(n):  # 오른쪽 포인터 : i

    # 작거나 같은 경우
    # 문제마다 다른 코드 작성

    # temp 설정 | 문제마다 다른 코드
    temp += arr[i]

    # 큰 경우
    if temp > s:

        # 큰 경우이고 오른쪽 포인터가 앞에 있을 때까지 조회
        while temp > s and i > start:
            # 조건 만족시 코드 작성
            # 문제마다 다른 코드
            temp -= arr[start]
            start += 1

        # 작거나 같은 경우, 포인터가 겹치는 경우
        # 문제마다 다른 코드 작성

print(ans)
