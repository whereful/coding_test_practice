# https://brownbears.tistory.com/467

n = int(input())

print(bin(n))  # 0b가 붙은 문자열 출력
print(oct(n))  # 0o가 붙은 문자열 출력
print(hex(n))  # 0x가 붙은 문자열 출력


print(int(bin(n), 2))  # 0b가 붙은 문자열을 다시 10진수로 변형할 수 있다
print(int(oct(n), 8))
print(int(hex(n), 16))


arr = ["10110", "1010", "11110"]
answer = 0
for a in arr:
    answer ^= int('0b' + a, 2)
