# two pointer

n = int(input())
arr = sorted(map(int, input().split()))

left = 0
right = n - 1

ans = [0, 0]
while left < right:
    ans[1] += arr[right]
    ans[0] += arr[left]

    right -= 1
    left += 1

if left == right:
    ans[1] += arr[right]

print(*ans)
