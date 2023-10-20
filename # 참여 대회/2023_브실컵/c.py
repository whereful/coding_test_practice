li = input().split('-')

before = 360 * int(li[0]) + 30 * (int(li[1]) - 1) + int(li[2]) - 1

after = before + int(input())

# print(before, after)
res = [after // 360, (after % 360) // 30 + 1, (after % 360) % 30 + 1]

print('%d-%02d-%02d' % (res[0], res[1], res[2]))
