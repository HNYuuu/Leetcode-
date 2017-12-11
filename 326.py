from math import log

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        elif n == 1:
            return True
        return n == 3**round(log(n,3))

print(Solution().isPowerOfThree(-3))