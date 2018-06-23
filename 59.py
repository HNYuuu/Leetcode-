class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        up, left = 0, 0
        right, bottom = n, n
        i, j = 0, 0
        count = 1
        while True:
            for j in range(left, right):
                matrix[i][j] = count
                count += 1
            up += 1

            if up >= bottom:
                break

            for i in range(up, bottom):
                matrix[i][j] = count
                count += 1
            right -= 1

            if left >= right:
                break

            for j in range(right - 1, left - 1, -1):
                matrix[i][j] = count
                count += 1
            bottom -= 1

            if up >= bottom:
                break

            for i in range(bottom - 1, up - 1, -1):
                matrix[i][j] = count
                count += 1
            left += 1

            if left >= right:
                break

        return matrix

print(Solution().generateMatrix(1))