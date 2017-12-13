import math

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        root = int(math.sqrt(num))
        divisors = [1]
        i = 2
        while i <= root:
            if num%i == 0:
                divisors.append(i)
                divisors.append(num//i)
            i += 1
        return True if sum(divisors) == num else False



print(Solution().checkPerfectNumber(28))