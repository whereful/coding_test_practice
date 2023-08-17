# 문자열 비교는 아스키 코드 순 == 사전 순

# x ** 3을 하는 이유는 0 ~ 999까지이기 때문에 자리수를 맞추기 위함

# 9 vs 10 ==> 999 vs 101010, 101 vs 105 ==> 101101101 vs 105105105

# [0, 0, 0, 0]의 경우에는 0을 출력해야 함
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
