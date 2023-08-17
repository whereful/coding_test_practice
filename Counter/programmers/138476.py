from collections import Counter


def solution(k, tangerine):
    arr = Counter(tangerine).most_common()

    answer, su = 0, 0
    for i in range(len(arr)):
        if su >= k:
            break
        else:
            su += arr[i][1]
            answer += 1
    # 반복문 내에서 return되지 않는 경우도 고려해야 함
    return answer
