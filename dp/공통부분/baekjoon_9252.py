'''
# comment

# 백준 9251과 유형 동일

'''

s = input()
n = len(s)

p = input()
m = len(p)


# 0 대신 ''로 정의하여 문자열 저장
# store[i][j] = ''
# 리스트로 정의 시 pypy3, python3에서 메모리 초과 발생
# python3으로 제출 시 시간초과 발생
store = [[''] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i - 1] == p[j - 1]:
            store[i][j] = store[i - 1][j - 1] + s[i - 1]
        else:
            if len(store[i - 1][j]) > len(store[i][j - 1]):
                store[i][j] = store[i - 1][j]
            else:
                store[i][j] = store[i][j - 1]


print(len(store[n][m]))
print(store[n][m])
