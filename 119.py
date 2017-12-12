import math

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        result = [0]*(rowIndex+1)

        def C(i, k):
            return math.factorial(k)//(math.factorial(k-i)*math.factorial(i))

        for i in range(math.ceil(rowIndex/2)+1):
            result[i] = C(i, rowIndex)

        # odd
        if rowIndex%2 == 0:
            result[rowIndex//2+1:] = result[:rowIndex//2][::-1]
        # even
        else:
            result[rowIndex//2+1:] = result[:rowIndex//2+1][::-1]

        return result

print(Solution().getRow(5))