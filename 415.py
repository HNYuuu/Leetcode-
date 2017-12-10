class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1Int = 0
        num2Int = 0
        for i in range(len(num1)):
            num1Int += (ord(num1[i])-48) * (10**(len(num1)-i-1))
        for i in range(len(num2)):
            num2Int += (ord(num2[i])-48) * (10**(len(num2)-i-1))
        return str(num1Int + num2Int)

print(Solution().addStrings('12345', '54321'))