class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(1+8*n)-1)//2)