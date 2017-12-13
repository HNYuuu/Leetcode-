import math

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x == 10:
            return False
        elif x < 10:
            return True
        length = math.ceil(math.log(x, 10))
        j = 10**(length-1)
        while j != 1 and j != 0:
            if x//j != x%10:
                return False
            else:
                x = x%j
                x = x//10
                j = j//100
        return True

print(Solution().isPalindrome(10))