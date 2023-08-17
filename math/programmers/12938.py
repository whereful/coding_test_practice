def solution(n, s):
    if s < n:
        return [-1]

    k = s // n
    r = s % n  # s - n * k

    ans = [k for i in range(n)]

    for i in range(r):
        ans[i] += 1

    return sorted(ans)
