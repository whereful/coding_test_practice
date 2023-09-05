# https://oranz.tistory.com/41

n, s = map(int, input().split())
arr = list(map(int, input().split()))

temp = 0  # 합을 저장하는 공간 temp

start = 0  # 왼쪽 포인터 start

ans = 0  # 개수 저장 ans

for i in range(n):  # 오른쪽 포인터 : i

    # 작거나 같은 경우

    temp += arr[i]

    # 문제에서 같은 경우만 고려하므로 같은 경우에 대한 코드 작성
    if temp == s:
        print(start, i)
        ans += 1

    # 큰 경우
    if temp > s:

        # 큰 경우
        while temp > s and i > start:
            temp -= arr[start]
            start += 1

        # 작거나 같은 경우
        # 문제에서 같은 경우만 고려하므로 같은 경우에 대한 코드 작성
        if temp == s:
            print(start, i)
            ans += 1

print(ans)
