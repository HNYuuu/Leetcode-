class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10

        result = 10
        tmp = 9
        for i in range(2, min(n+1,11)):
            tmp *= (11-i)
            result += tmp
        return result

print(Solution().countNumbersWithUniqueDigits(4))