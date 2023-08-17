arr = list(map(int, input().split()))

for i in range(1, len(arr) - 1 + 1):
    arr[i] = arr[i] + arr[i - 1]

print(arr)
