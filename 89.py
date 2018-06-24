class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(2**n):
            result.append(i^(i>>1))

        return result

print(Solution().grayCode(0))