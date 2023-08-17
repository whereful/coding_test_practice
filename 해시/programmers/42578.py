from collections import defaultdict


def solution(clothes):
    answer = 1

    # 한 번도 선택하지 않은 경우의 수 1을 기본값으로 설정
    info = defaultdict(lambda: 1)
    for cl, ty in clothes:
        info[ty] += 1

    for v in info.values():
        answer *= v

    return answer - 1
