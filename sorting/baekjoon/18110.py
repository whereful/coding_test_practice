'''
# https://m.blog.naver.com/youndok/222218536425

# https://www.acmicpc.net/source/63220342
'''

'''
import statistics
import sys
from decimal import ROUND_HALF_UP, getcontext, Decimal
getcontext().rounding = ROUND_HALF_UP


def input(): return sys.stdin.readline().strip()

# # Decimal(str()).quantize(str('원하는 수 형태')) -> int() or float()로 묶기


n = int(input())
arr = sorted([int(input()) for _ in range(n)])

s = int(Decimal(str(n * 0.15)).quantize(Decimal("1")))
if n == 0:
    print(0)
elif n in (1, 2, 3):
    print(Decimal(str(statistics.mean(arr))).quantize(Decimal("1")))
else:
    print(Decimal(str(statistics.mean(arr[s:-s]))).quantize(Decimal("1")))
'''


def input(): return sys.stdin.readline().strip()


n = int(input())
arr = [int(input()) for _ in range(n)]

try:
    k = int(n * 0.15 + 0.5)
    print(int(sum(sorted(arr)[k: n - k]) / (n - 2 * k) + 0.5))
except:
    print(0)
