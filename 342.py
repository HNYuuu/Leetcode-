class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        binnum = bin(num)[2:]
        if binnum[0] == '1' and binnum[1:].count('0') == len(binnum)-1 and (len(binnum)-1) % 2 == 0:
            return True
        else:
            return False
        
print(Solution().isPowerOfFour(16))