from collections import deque


def solution(numbers, direction):
    numbers = deque(numbers)

    # rotate 함수 존재
    numbers.rotate(1 if direction == 'right' else -1)
    return list(numbers)
