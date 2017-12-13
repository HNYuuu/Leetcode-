class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        result = 0
        while n//5 != 0:
            result += n//5
            n = n//5
        return result

print(Solution().trailingZeroes(34567876545678))