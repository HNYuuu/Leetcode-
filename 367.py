class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = num
        m = (r-l)//2+l
        while l <= r:
            if m*m > num:
                r = m-1
            elif m*m < num:
                l = m+1
            else:
                return True
            m = (r-l)//2+l
        return False

print(Solution().isPerfectSquare(0))