# 에라토스테네스의 체 코드 이용

n = int(input())

# 1과 자기 자신 약수 개수 선정 - i일 때는 i * 2를 증가시켜서 중복 증가 우려 없음
arr = [2] * (n + 1)
arr[0], arr[1] = 0, 1

# 시간복잡도 : n log n으로 추정
for i in range(2, n + 1):
    # i의 배수는 i를 약수로 가지고 있으므로 +1을 시킴
    for j in range(i * 2, n + 1, i):
        arr[j] += 1

# 여기서 arr[i] == 2를 만족하는 i만 소수임

print(arr)
