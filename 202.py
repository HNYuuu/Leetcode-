class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tempSet = set()

        def sumSquare(x):
            x = str(x)
            tempList = [i for i in x]
            tempSum = sum([int(i)**2 for i in tempList])
            return tempSum

        n = sumSquare(n)
        while n != 1:
            if n not in tempSet:
                tempSet.add(n)
            else:
                return False
            n = sumSquare(n)
        return True

print(Solution().isHappy(256))