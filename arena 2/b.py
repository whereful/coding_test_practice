import sys
def input(): return sys.stdin.readline().strip()


def check(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0 and i % 5 != 0:
        return "Fizz"
    elif i % 3 != 0 and i % 5 == 0:
        return "Buzz"
    else:
        return i


arr = [input() for _ in range(3)]

for k in range(3):
    if arr[k].isdigit():
        print(check(int(arr[k]) + 3 - k))
        exit(0)
