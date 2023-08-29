'''
# comment

양쪽 끝에서 가운데로 좁혀지는 방식으로
회문 여부 판별

회문 불가로 판별된 지점에서 2가지 경우로 
나누어서 다시 진행

'''


def isPalin_left(s):

    left = 0
    right = len(s) - 1

    isPalin = 0
    coin = 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif coin == 1:
            left += 1

            coin = 0
            isPalin += 1
        else:
            return 2

    return isPalin


def isPalin_right(s):

    left = 0
    right = len(s) - 1

    isPalin = 0
    coin = 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif coin == 1:
            right -= 1

            coin = 0
            isPalin += 1
        else:
            return 2

    return isPalin


for _ in range(int(input())):
    s = input()
    print(min(isPalin_left(s), isPalin_right(s)))
