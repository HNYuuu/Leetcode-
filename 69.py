class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        delta = 0.1
        xn = 1
        pre = xn
        xm = (xn**2+x)/(2*xn)
        while abs(xm-xn) > delta:
            pre = xm
            xn = xm
            xm = (xn**2+x)/(2*xn)
        return int(xm)

print(Solution().mySqrt(8))