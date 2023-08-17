'''
# https://m.blog.naver.com/youndok/222218536425

# https://www.acmicpc.net/source/63220342
'''

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = [int(input()) for _ in range(n)]

try:
    k = int(n * 0.15 + 0.5)
    print(int(sum(sorted(arr)[k: n - k]) / (n - 2 * k) + 0.5))
except:
    print(0)
