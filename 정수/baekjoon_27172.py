'''
# comment



'''

n = int(input())

# 원본
arr = list(map(int, input().split()))

# 가장 큰 수 설정
max = max(arr)

# 에라토스테네스 체를 순회할 때 탐색 원소가 arr에 존재하는지를 확인하기 위해 선언한 집합
arr_set = set(arr)

# 에라토스테네스의 체 변형
point = [0] * (max + 1)

# 배열이 나타난 범위에서 살펴봄
for i in sorted(arr):

    multiple = 2

    # 집합 범위 내에서
    while i * multiple <= max:
        # 해당 배수들이 집합에 존재한다면 포인트 수정
        if i * multiple in arr_set:
            point[i] += 1
            point[i * multiple] -= 1

        multiple += 1

for a in arr:
    print(point[a], end=' ')
