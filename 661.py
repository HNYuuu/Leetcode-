# image smoother

def solution(matrix):
    dimention_v = len(matrix)
    dimention_h = len(matrix[0])
    result = [[0 for i in range(dimention_h)] for i in range(dimention_v)]
    # modify the matrix to simplify the calculate
    for i in matrix:
        i.insert(0,-1)
        i.append(-1)
    matrix.insert(0, [-1 for i in range(dimention_h+2)])
    matrix.append([-1 for i in range(dimention_h+2)])
    # smooth
    for i in range(1,dimention_v+1):
        for j in range(1,dimention_h+1):
            minus_one = 0
            minus_one += matrix[i-1][j-1:j+2].count(-1)
            minus_one += matrix[i][j-1:j+2].count(-1)
            minus_one += matrix[i+1][j-1:j+2].count(-1)
            s = sum(matrix[i-1][j-1:j+2])+sum(matrix[i][j-1:j+2])+sum(matrix[i+1][j-1:j+2])+minus_one
            result[i-1][j-1] = s//(9-minus_one)
    return result

if __name__ == '__main__':
    print(solution([[1]]))