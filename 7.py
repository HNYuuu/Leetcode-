class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        numStr = str(x)
        minus = True if x < 0 else False

        numList = [i for i in numStr]
        numList.reverse()
        while numList[0] == '0':
            numList.pop(0)

        if not minus:
            numReStr = "".join(numList)
        else:
            numReStr = "".join(numList[:-1])
            numReStr = '-' + numReStr
        numRe = int(numReStr)
        if numRe > 2147483647 or numRe < -2147483648:
            return 0
        return numRe

print(Solution().reverse(-12345))