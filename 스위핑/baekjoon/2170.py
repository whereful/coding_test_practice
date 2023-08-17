# https://www.acmicpc.net/source/54547355


from sys import stdin

n = int(stdin.readline())
lines = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

# 시작점을 기준으로 정렬한다
lines.sort(key=lambda t: t[0])
result = 0
start, end = lines[0][0], lines[0][1]
for line in lines:

    # 새로운 시작점이 기존 끝점보다 더 크면 새로운 라인을 기준으로 설정한다
    if line[0] > end:
        # 기존에 구한 시작점, 끝점을 더한다
        result += end - start
        start, end = line
    # 기존 끝점보다 더 큰 끝점이 나오면 확장한다
    if line[1] > end:
        end = line[1]

# 최종적으로 구한 시작점, 끝점의 차이를 더한다
result += end - start
print(result)
