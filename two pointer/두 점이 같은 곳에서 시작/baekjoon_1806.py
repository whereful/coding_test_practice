# https://oranz.tistory.com/41

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = n + 1
temp = 0
start = 0

# 오른쪽 포인터 : i
for i in range(n):

    # 합을 저장하는 공간 temp
    temp += arr[i]

    # 문제에서 크거나 같은 경우를 따지므로 같은 경우에 대한 코드 작성
    if temp == s:
        ans = min(ans, i - start + 1)

    # 큰 경우
    if temp > s:
        while temp > s and i > start:
            # 문제에서 크거나 같은 경우를 따지므로 큰 경우에 대한 코드 작성
            ans = min(ans, i - start + 1)
            temp -= arr[start]
            start += 1

        # 문제에서 크거나 같은 경우를 따지므로 같은 경우에 대한 코드 작성
        if temp == s:
            ans = min(ans, i - start + 1)

# n + 1 길이는 존재할 수 없음
print(0 if ans > n else ans)
