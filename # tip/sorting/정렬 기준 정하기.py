'''
문제 

"221123" 같은 문자열이 주어짐

0 ~ 9까지 많이 등장한 순으로 정렬하여 출력

출력 : "2 1 3 0 4 5 6 7 8 9"

'''


def solution(s):

    # 등장 개수가 많은 순서대로 출력 - lambda로 설정할 경우 값이 같으면 먼저 등장한 순서대로 정렬(즉, 순서를 바꾸지 않음)
    a = sorted([i for i in range(0, 9 + 1)], key=lambda x: -s.count(str(x)))
    return ' '.join(map(str, a))
