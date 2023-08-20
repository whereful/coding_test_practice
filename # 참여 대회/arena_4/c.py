import sys
def input(): return sys.stdin.readline().strip()


n, m, k = map(int, input().split())

# 입력으로 들어오는 문자열도 정렬해야 함
arr = sorted([''.join(sorted(input())) for _ in range(n)])

s = ''
for i in range(k):
    s += arr[i]

print(''.join(sorted(s)))
