'''
# comment

[n / 3] == int((n - 1) // 3 + 1)
'''

import sys
def input(): return sys.stdin.readline().strip()


def prefix(s):
    return s[0:int((len(s) - 1) // 3 + 1) - 1 + 1]


def tail(s):
    return s[1:]


def rev(s):
    return s[::-1]


for _ in range(int(input())):
    s = input()
    ps = prefix(s)

    # print(s, ps)

    if s == ps + rev(ps) + ps:
        print(1)
        continue
    elif s == ps + tail(rev(ps)) + ps:
        print(1)
        continue
    elif s == ps + rev(ps) + tail(ps):
        print(1)
        continue
    elif s == ps + tail(rev(ps)) + tail(ps):
        print(1)
        continue
    else:
        print(0)
