# m * l 행렬 X l * n 행렬 = m * n 행렬

def solution(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in list(zip(*B))] for A_row in A]
