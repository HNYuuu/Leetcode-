class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        remainder = []
        minus = True if num < 0 else False
        if minus:
            num = -num
        while num//7 != 0:
            remainder.append(str(num%7))
            num = num//7
        remainder.append(str(num))
        remainder.reverse()
        if not minus:
            return "".join(remainder)
        else:
            return '-'+"".join(remainder)

print(Solution().convertToBase7(-1))