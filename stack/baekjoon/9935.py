'''
# comment

# https://hwayomingdlog.tistory.com/134?category=939394

# replace 함수 시간복잡도

# https://velog.io/@heejun32/%EB%B0%B1%EC%A4%80-9935%EB%B2%88-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AD%EB%B0%9C-Python

'''


s = input()
p = input()
lp = len(p)

stack = []

# 스택에 넣은 다음에 처리
for i in range(len(s)):

    stack.append(s[i])
    if ''.join(stack[-lp:]) == p:
        for _ in range(lp):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')
