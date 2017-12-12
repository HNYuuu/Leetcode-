class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        i = 1
        while i < numRows:
            temp = [1]
            for j in range(1,i):
                temp.append(result[i-1][j]+result[i-1][j-1])
            temp.append(1)
            result.append(temp)
            i += 1
        return result

print(Solution().generate(4))
