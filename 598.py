# range addition II

def solution(m, n, ops):
    if len(ops) == 0:
        return m*n
    op = list(zip(*ops))
    return min(op[0]) * min(op[1])