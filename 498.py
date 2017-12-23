# 给定一个二维数组, 沿对角线遍历这个矩阵. 一开始没有考虑
# 边界条件, 只是把所有可能的遍历一遍, 但是一旦给出一个很
# 长的一维向量就会很浪费时间, 然后优化了一下将 i 和 j 
# 的起始值修改, 边界条件检查更加严格

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        M = len(matrix)
        N = len(matrix[0])
        result = []
        total = 0
        while total < M+N-1:
            for i in range(min(M-1, total), -1, -1):
                j = total - i
                if j == N:
                    break
                result.append(matrix[i][j])
            total += 1
            if total > M+N-2:
                break
            for j in range(min(N-1, total), -1, -1):
                i = total - j
                if i == M:
                    break
                result.append(matrix[i][j])
            total += 1
        return result

print(Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [10, 11, 12]
]))
