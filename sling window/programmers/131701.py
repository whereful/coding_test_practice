# 누적합을 이동 - 슬라이싱 윈도우
def solution(elements):
    n = len(elements)
    arr = elements + elements

    answer = set()

    for l in range(1, n + 1):
        for i in range(0, n - 1 + 1):
            if i == 0:
                su = sum(arr[:l])
            else:
                # 그 전 원소를 빼야 함
                su = su - arr[i - 1] + arr[i + l - 1]
            answer.add(su)

    return len(answer)
