import sys
def input(): return sys.stdin.readline().strip()


f = []
while True:
    s = input()

    if s == '=':
        break

    f.append(s)

ans, f = int(f[0]), f[1:]

# print(ans, f)

for i in range(0, len(f) - 1 + 1, 2):
    if f[i] == '+':
        ans += int(f[i + 1])
    elif f[i] == '-':
        ans -= int(f[i + 1])
    elif f[i] == '*':
        ans *= int(f[i + 1])
    else:
        ans //= int(f[i + 1])

print(ans)
