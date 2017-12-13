# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        m = (h-l)//2+l
        while l <= h:
            result = guess(m)
            if result == 0:
                return m
            elif result == 1:
                l = m+1
            else:
                h = m-1
            m = (h-l)//2+l
        return m