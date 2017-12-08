class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nLeft = n << 1
        result = nLeft ^ n
        for i in bin(result)[2:-1]:
            if i == '0':
                return False
        return True