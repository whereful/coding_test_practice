n = int(input())


def check(num):
    if num == 300:
        return 1
    elif 275 <= num < 300:
        return 2
    elif 250 <= num < 275:
        return 3
    elif num < 250:
        return 4


print(*[check(a) for a in list(map(int, input().split()))])
