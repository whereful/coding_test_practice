import sys
def input(): return sys.stdin.readline().strip()


today = input()
print(sum([input() >= today for _ in range(int(input()))]))
