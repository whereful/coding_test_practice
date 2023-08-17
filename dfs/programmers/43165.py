# 시간 복잡도 : 2 ** 숫자의 개수

# 트리라고 생각하면 됨
def solution(numbers, target):

    def dfs(node, i):
        # 리프 노드에 도달하면 타겟이 되었는지 확인
        if len(numbers) == i:
            return node == target

        # dfs(0, 0)에서 타겟의 개수는 왼쪽 서브 트리의 개수 + 오른쪽 서브 트리의 개수
        return dfs(node + numbers[i], i + 1) + dfs(node - numbers[i], i + 1)

    return dfs(0, 0)
