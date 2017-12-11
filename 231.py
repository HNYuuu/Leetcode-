class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        binN = bin(n)[2:]
        for i in binN[1:]:
            if i == '1':
                return False
        return True

print(Solution().isPowerOfTwo(3))