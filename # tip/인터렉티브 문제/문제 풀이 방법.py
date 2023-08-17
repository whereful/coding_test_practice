import sys
def input(): return sys.stdin.readline().strip()


arr = ["bowling", "swimming", "soccer"]

n = int(input())
for i in range(n):
    print(arr[i % 3], end=' ')
print()

sys.stdout.flush()

arr2 = input().split()

for i in range(n):
    a = list(set(["bowling", "swimming", "soccer"]) -
             set([arr[i % 3], arr2[i]]))  # 입력받은 거는 순서대로 주어져서 다 살펴봐야 함
    print(a[0], end=' ')

print()

sys.stdout.flush()

# 그냥 입력, 출력 밑에 sys.stdout.flush() 적으면 됨
