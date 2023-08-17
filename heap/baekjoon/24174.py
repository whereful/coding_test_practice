import sys
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 6)


def reverse_heap_sort(A, n):
    min_heap(A, n)

    # for문 역순에서는 -1을 붙여야 내가 원하는 범위까지 작동함
    for i in range(n, 2 - 1, -1):
        A[1], A[i] = A[i], A[1]

        # 교환 횟수 증가하고 최대치에 도달하면 종료
        global count
        count += 1
        if (count == change):
            print(*A[1:])
            exit(0)

        heapify(A, 1, i - 1)


def min_heap(A, n):
    # 역순에서는 -1을 붙여야 내가 원하는 범위까지 작동함
    for i in range(n // 2, 1 - 1, -1):
        heapify(A, i, n)


# k번째 인덱스를 부모로하는 서브트리가 최소 힙을 만족하게 하려는 함수
# n은 배열의 끝 인덱스
def heapify(A, k, n):

    left = 2 * k
    right = 2 * k + 1

    # smaller 변수에 임의의 값 설정
    smaller = -1

    # 자식이 2개인 경우
    if (right <= n):
        # 더 작은 값을 가진 인덱스를 smaller로 설정
        smaller = left if A[left] < A[right] else right
    # 자식이 1개인 경우
    elif (left <= n):
        smaller = left
    # 자식이 없는 경우 종료
    else:
        return

    # k번째 인덱스 자식들도 살펴봐야 함
    if (A[smaller] < A[k]):
        A[k], A[smaller] = A[smaller], A[k]

        # 교환 횟수 증가하고 최대치에 도달하면 종료
        global count
        count += 1
        if (count == change):
            print(*A[1:])
            exit(0)

        heapify(A, smaller, n)


n, change = map(int, input().split())
# 교환 횟수를 저장하는 변수
count = 0

# 0번째 인덱스는 사용하지 않음
arr = [0] + list(map(int, input().split()))

reverse_heap_sort(arr, n)

print(-1)
