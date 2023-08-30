li = list(input())

for i in range(0, len(li) + 1):
    # 기존 문자열에다가 접두사를 뒤집은 것을 붙임
    target = li + li[:i][::-1]

    # 새로 만든 문자열이 팰린드롬인지 확인
    if target == target[::-1]:
        print(len(target))
        exit(0)
