arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# (a, b) ~ (c, d) 부분 추출(인덱스 0 기준)
a, b, c, d = map(int, input().split())
part = [arr[i][b:d + 1] for i in range(a, c+1)]
