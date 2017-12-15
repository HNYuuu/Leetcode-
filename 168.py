class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n != 0:
            remainder = n%26
            if remainder == 0:
                result.insert(0, 'Z')
                n = n//26-1
            else:
                result.insert(0, chr(remainder+64))
                n = n//26
        return "".join(result)            


print(Solution().convertToTitle(10000))
