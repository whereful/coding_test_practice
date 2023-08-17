# 스택은 원소를 치환하는 관점

from math import ceil
from collections import Counter


def solution(progresses, speeds):

    arr = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    for i in range(1, len(arr)):
        arr[i] = max(arr[i - 1], arr[i])

    return [value for key, value in Counter(arr).items()]
