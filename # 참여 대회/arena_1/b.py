def main():
    N = int(input())
    S = [input() for _ in range(N)]

    q = S.index("?")

    M = int(input())
    for _ in range(M):
        a = input()
        if a in S:
            continue
        # q - 1이 예외가 안 생기는 상황 고려
        if q != 0 and S[q - 1][-1] != a[0]:
            continue
        # q + 1이 예외가 안 생기는 상황 고려
        if q != N - 1 and a[-1] != S[q + 1][0]:
            continue
        print(a)


if __name__ == "__main__":
    main()
