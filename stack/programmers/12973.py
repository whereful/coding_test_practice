# 없앤다 == ''로 치환 -> 스택
def solution(s):
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return int(len(stack) == 0)
