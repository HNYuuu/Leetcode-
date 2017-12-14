import math

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        divisorLimit = math.ceil(math.sqrt(c))
        possible = set()
        for i in range(0, divisorLimit+1):
            possible.add(i**2)
        for i in possible:
            if c-i in possible:
                return True
        return False

print(Solution().judgeSquareSum(4))