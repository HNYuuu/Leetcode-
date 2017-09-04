# range addition II

def solution(m, n, ops):
    op = list(zip(*ops))
    return min(op[0]) * min(op[1])