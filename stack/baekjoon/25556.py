import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))

stacks = [[] for _ in range(4)]

for a in arr:
    possible = False

    for i in range(0, 3 + 1):

        if not stacks[i] or stacks[i][-1] < a:
            stacks[i].append(a)
            possible = True
            break

    if possible == False:
        print('NO')
        exit(0)

print('YES')
