class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # if gcd(x,y) is prime, getting the water is easy
        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            if b == 0:
                return a
            else:
                return gcd(b, a%b)

        if z > x+y:
            return False
        factor = gcd(x, y)
        if factor == 1:
            return True
        elif factor == 0:
            return True
        elif z % factor == 0:
            return True
        else:
            return False


print(Solution().canMeasureWater(1,2,3))