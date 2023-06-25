'''
# comment

완전이진트리 부모 노드 번호

자식 = 2k + 1, 2k -> k

# https://calssess.tistory.com/91
'''

import sys
def input(): return sys.stdin.readline().strip()

# 자기 자신과 부모를 저장하는 리스트


def find_parent(parent_list, n):

    while True:
        parent_list.append(n)

        n = n // 2

        if n == 0:
            break


for _ in range(int(input())):
    a, b = map(int, input().split())

    parent_a = []
    parent_b = []

    find_parent(parent_a, a)
    find_parent(parent_b, b)

    # print(parent_a)
    # print(parent_b)

    print(max(set(parent_a) & set(parent_b)) * 10)
