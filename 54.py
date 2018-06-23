class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        
        result = []
        up, left = 0, 0
        right, bottom = len(matrix[0]), len(matrix)
        i, j = 0, 0
        while True:
            for j in range(left, right):
                result.append(matrix[i][j])
            up += 1

            if up >= bottom:
                break

            for i in range(up, bottom):
                result.append(matrix[i][j])
            right -= 1

            if left >= right:
                break

            for j in range(right-1, left-1, -1):
                result.append(matrix[i][j])
            bottom -= 1

            if up >= bottom:
                break

            for i in range(bottom-1, up-1, -1):
                result.append(matrix[i][j])
            left += 1

            if left >= right:
                break

            # print(left, right, up, bottom)

        return result

print(Solution().spiralOrder([
 [ 1, 2, 3 ],
 # [ 4, 5, 6 ],
 # [ 7, 8, 9 ]
]))