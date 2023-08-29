import sys
def input(): return sys.stdin.readline().strip()


min_x, min_y, max_x, max_y = -sys.maxsize, - \
    sys.maxsize, sys.maxsize, sys.maxsize

for _ in range(int(input())):

    co = input().split()

    if co[2] == 'L':
        max_x = min(max_x, int(co[0]) - 1)

        # print(max_x)
    elif co[2] == 'R':
        min_x = max(min_x, int(co[0]) + 1)

        # print(min_x)
    elif co[2] == 'U':
        min_y = max(min_y, int(co[1]) + 1)
        # print(min_y)
    elif co[2] == 'D':
        max_y = min(max_y, int(co[1]) - 1)
        # print(max_y)

# print(min_x, max_x, min_y, max_y)

if -sys.maxsize not in (min_x, min_y) and sys.maxsize not in (max_x, max_y):
    print((max_x - min_x + 1) * (max_y - min_y + 1))
else:
    print('Infinity')
