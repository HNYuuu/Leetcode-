# baseball game

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = []
        for i in ops:
            if i != 'C' and i != 'D' and i != '+':
                result.append(int(i))
            elif i == 'C':
                result.pop()
            elif i == 'D':
                result.append(result[-1]*2)
            else:
                result.append(result[-1]+result[-2])
        return sum(result)

s = Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))