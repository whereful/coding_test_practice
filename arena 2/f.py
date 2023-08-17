# https://solved.ac/arena/2/editorial

import sys
def input(): return sys.stdin.readline().strip()


def calc(op, a, v):
    if op == '+':
        return (a + v) % 7
    if op == '*':
        return (a * v) % 7


for _ in range(int(input())):
    n = int(input())

    dp = [[0] * 7 for _ in range(n + 1)]
    dp[0][1] = 1

    for i in range(n):
        # op1, v1, op2, v2 = input().split()
        # v1, v2 = int(v1), int(v2)

        ope = input().split()

        # for j in range(0, 6 + 1):
        '''
            if dp[i][j] == 1:
                dp[i + 1][calc(op1, j, v1)] = 1
                dp[i + 1][calc(op2, j, v2)] = 1
            '''

        '''
            dp[i + 1][calc(op1, j, v1)] = max(dp[i + 1]
                                              [calc(op1, j, v1)], dp[i][j])
            dp[i + 1][calc(op2, j, v2)] = max(dp[i + 1]
                                              [calc(op2, j, v2)], dp[i][j])
            '''

        if ope[0] == '+':
            for j in range(0, 6 + 1):
                # dp[i + 1][(j + int(ope[1])) % 7] += dp[i][j]
                dp[i + 1][(j + int(ope[1])) % 7] = max(dp[i + 1]
                                                       [(j + int(ope[1])) % 7], dp[i][j])
        elif ope[0] == '*':
            for j in range(0, 6 + 1):
                # dp[i + 1][(j * int(ope[1])) % 7] += dp[i][j]
                dp[i + 1][(j * int(ope[1])) % 7] = max(dp[i + 1]
                                                       [(j * int(ope[1])) % 7], dp[i][j])
        if ope[2] == '+':
            for j in range(0, 6 + 1):
                # dp[i + 1][(j + int(ope[3])) % 7] += dp[i][j]
                dp[i + 1][(j + int(ope[3])) % 7] = max(dp[i + 1]
                                                       [(j + int(ope[3])) % 7], dp[i][j])
        elif ope[2] == '*':
            for j in range(0, 6 + 1):
                # dp[i + 1][(j * int(ope[3])) % 7] += dp[i][j]
                dp[i + 1][(j * int(ope[3])) % 7] = max(dp[i + 1]
                                                       [(j * int(ope[3])) % 7], dp[i][j])

    print("LUCKY" if dp[n][0] > 0 else "UNLUCKY")
