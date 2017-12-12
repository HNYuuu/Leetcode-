class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                continue
            elif num % 3 == 0:
                num = num // 3
                continue
            elif num % 5 == 0:
                num = num // 5
                continue
            break
        return True if num == 1 else False
            