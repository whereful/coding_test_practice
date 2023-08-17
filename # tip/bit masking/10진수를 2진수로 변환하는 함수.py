# https://brownbears.tistory.com/467

n = int(input())

print(bin(n))  # 0b
print(oct(n))  # 0o
print(hex(n))  # 0x

print(int(bin(n), 2))
print(int(oct(n), 8))
print(int(hex(n), 16))
