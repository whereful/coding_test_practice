import sys
def input(): return sys.stdin.readline().strip()


def check(num):
    if num < 60:
        return 0
    elif 60 <= num < 100:
        return 1
    elif 100 <= num < 140:
        return 2
    elif 140 <= num < 200:
        return 3
    elif 200 <= num < 250:
        return 4
    elif 250 <= num:
        return 5


n = int(input())
levels = sorted([int(input()) for _ in range(n)], reverse=True)

print(sum(levels[:42]), sum([check(a) for a in levels[:42]]))
