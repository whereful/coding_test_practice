

def solution(t, p):
    return len([i for i in range(len(t) - len(p) + 1) if int(t[i:i+len(p)]) <= int(p)])
