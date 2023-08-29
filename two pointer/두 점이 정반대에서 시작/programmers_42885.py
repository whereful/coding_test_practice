# 최적의 해는 합이 최대한 limit에 가까워야 함 - 그래서 양옆에서 대응시킴
def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:

        # 합이 대응되면 왼쪽 증가
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1

        # 합이 대응되지 않으면 왼쪽은 고정시키고 오른쪽 감소(합이 대응되어도 오른쪽 감소는 동일함)
        # 작은 것을 최대한 대응시켜야 함
        b -= 1
    return len(people) - answer
