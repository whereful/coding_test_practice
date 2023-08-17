from collections import defaultdict

arr = [int(input()) for _ in range(5)]
dic = defaultdict(int)

for a in arr:
    dic[a] += 1

for d in dic.keys():
    if dic[d] % 2 == 1:
        print(d)
        exit(0)
