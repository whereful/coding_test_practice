
# 첫 원소가 0보다 크면 1, 4분면인것이 정해짐
def solution(dot):
    quad = [(3, 2), (4, 1)]
    return quad[dot[0] > 0][dot[1] > 0]
