class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # result = 0
        # i = 1
        # while i*i <= n:
        #     result += 1
        #     i += 1
        # return result
        return int(n**.5)


print(Solution().bulbSwitch(5))
