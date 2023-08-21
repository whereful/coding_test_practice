dir = {
    'S': 0,
    'E': 1,
    'N': 2,
    'W': 3
}

group = {
    'T': [['.', 'O'], ['P', '.']],
    'F': [['I', '.'], ['.', 'P']],
    'Lz': [['O', '.'], ['.', 'P']]
}

direction = input()
arr = [list(input()) for _ in range(2)]
for _ in range(dir[direction]):
    arr = list(map(list, zip(*arr[::-1])))

# print(arr)

for k, v in group.items():
    if arr == v:
        print(k)
        exit(0)

print('?')
