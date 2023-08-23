'''
문제 

"221123" 같은 문자열이 주어짐

0 ~ 9까지 많이 등장한 순으로 정렬하여 출력

출력 : "2 1 3 0 4 5 6 7 8 9"

'''


def solution(s):
    a = sorted([i for i in range(0, 9 + 1)], key=lambda x: -s.count(str(x)))
    return ' '.join(map(str, a))
