def solution(sequence, k):

    start = 0
    temp = 0
    ans = []

    for i in range(len(sequence)):

        # 구하려는 값에 오른쪽 포인터 수를 더함
        temp += sequence[i]

        # 조건 만족하면 정답 리스트에 추가
        if temp == k:
            ans.append([start, i])

        # 합이 조건보다 큰 경우
        if temp > k:

            # 조건보다 크고 왼쪽 포인터가 더 왼쪽에 있을 때까지
            while temp > k and start < i:
                temp -= sequence[start]
                start += 1

            # 조건 만족하면 추가
            if temp == k:
                ans.append([start, i])

    return min(ans, key=lambda x: (x[1] - x[0]))
