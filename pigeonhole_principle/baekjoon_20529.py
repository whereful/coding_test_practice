'''
# comment

33개부터는 개수가 3인 mbti가 적어도 1개 이상 존재

'''

from itertools import combinations
import sys
def input(): return sys.stdin.readline().strip()


def count_different(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

    return count

    # return len(set(a) - set(b))


def all_distance(c):
    return count_different(c[0], c[1]) + count_different(c[1], c[2]) + \
        count_different(c[2], c[0])


for _ in range(int(input())):
    n = int(input())
    mbti_array = input().split()

    if n > 32:
        print(0)
        continue

    mbti_array_combinations = list(combinations(mbti_array, 3))

    answer = 1e11

    for m in mbti_array_combinations:
        answer = min(answer, all_distance(m))

    print(answer)
