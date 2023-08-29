input_number = int(input())
n = 2

while n <= input_number:
    if input_number % n == 0:
        print(n)
        input_number //= n
    else:
        n += 1
