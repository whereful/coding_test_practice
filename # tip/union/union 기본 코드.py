'''
# https://velog.io/@woo0_hooo/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-union-find-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

# https://0x15.tistory.com/34

두 블로그에 나온 코드는 잘못됨

union 코드에서 a = find(a), b = find(b), parent[b] = a를 하게 되면

7 6(노드, 간선 수)
1 6
6 3
3 5
4 1
2 4
4 7

예시에서 실제 부모는 [0, 1, 4, 6, 1, 3, 1, 4]이지만
부모 배열이 [0, 1, 1, 1, 1, 1, 1]이 저장됨(부모 대신 루트가 저장됨)

find 함수에서 경로 압축을 하지 않아도 부모 배열에 루트가 저장됨

즉, 부모에 루트가 저장하게 되는 원인은 a, b를 루트로 값을 바꾸었기 때문
'''

'''
그리고 블로그에 설명된 경로 압축 기법은 실제로 결과가 이상하게 나옴

def find_root(a):
    if a == parent[a]:
        return parent[a]
    # return find_root(parent[a])
    parent[a] = find_root(parent[a])
    return parent[a]

여기서 부모 배열에 루트를 저장하게 되면

7 6(노드, 간선 수)
1 6
6 3
3 5
4 1
2 4
4 7
예시에서 
부모 배열이 [0, 1, 1, 1, 1, 1, 1]로 되어야 하지만
결과가 [0, 1, 4, 1, 1, 3, 1, 4]로 설정

부모와 루트가 섞이는 결과가 발생

'''


# 루트 노드는 함수를 조회할 때마다 값 갱신
def find_root(a):
    if a == parent[a]:
        return parent[a]

    '''
    parent[a] = find_root(parent[a])
    return parent[a]

    이 코드는 부모 노드를 저장한 parent에 루트 노드를 저장하도록 변경해서 그래프가 변경됨
    '''
    return find_root(parent[a])


# 부모 재설정
# 루트 조회를 root[a]로 설정하는 게 확실하지 않음
def union(a, b):

    # 루트 노드를 따로 구분해야 함
    root_A = find_root(a)
    root_B = find_root(b)

    if root_A < root_B:
        # 부모 재설정
        parent[b] = a

    else:
        # 부모 재설정
        parent[a] = b


n = int(input())

# 1이 루트 노드
parent = [i for i in range(n + 1)]

# root 배열로 root 조회를 한 번에 할 수 있는지 확실하지 않음
# root = [i for i in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    union(a, b)

print(parent)
