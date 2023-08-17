def solution(arr, divisor):

    # 참이면 앞 반환, 거짓이면 뒤 반환
    return sorted([i for i in arr if i % divisor == 0]) or [-1]
