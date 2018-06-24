class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        left, right = 1, 1
        while True:

            if (2*q*right+q)%p == 0:
                left = 0
                break
            right += 1

            if (2*q*left)%p == 0:
                right = 0
                break
            left += 1


        if left != 0:
            return 2
        else:
            count = (2*q*right + q)//p
            if count%2 == 1:
                return 1
            else:
                return 0
print(Solution().mirrorReflection(3,2))