class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            if self.divideBySelf(i):
                result.append(i)
        return result

    def divideBySelf(self, number):
        numberStr = str(number)
        for i in numberStr:
            if i == '0' or number % int(i) != 0:
                return False
        return True

solution = Solution()
print(solution.selfDividingNumbers(1, 22))
