# https://www.acmicpc.net/problem/2239

# https://www.acmicpc.net/source/55499869

def search(depth):

    # depth 가 z 의 범위를 초과하였을 경우 스도쿠가 완성되었다는 의미이므로 출력 후 종료
    if depth == len(z):
        for s in sudoku:

            # map 함수로 배열 원소를 문자로 전환
            print(''.join(map(str, s)))
        exit(0)

    y, x = z[depth]

    # 가능한 숫자 후보군
    numbers = [True] * 10

    # 가로 세로 줄 탐색
    for i in range(9):
        # 스도쿠의 가로에 있는 숫자를 후보에서 제거
        numbers[sudoku[y][i]] = False
        numbers[sudoku[i][x]] = False

    # 사각형 탐색
    for i in range(3):
        for j in range(3):
            numbers[sudoku[(y // 3) * 3 + i][(x // 3) * 3 + j]] = False

    # 탐색해서 나오지 않은 숫자들을 모두 기록해보며 dfs
    for i in range(1, 9 + 1):
        if numbers[i]:

            # 스도쿠에 기록
            sudoku[y][x] = i
            search(depth + 1)

    # 탐색 종료 시 0으로 되돌리기 - 위로 올라갈 때 0으로 초기화해야 함
    sudoku[y][x] = 0


sudoku = [list(map(int, list(input()))) for _ in range(9)]

# 후보 좌표들을 1줄로 정의
z = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

# 0번째 노드 시작 탐색
search(0)
