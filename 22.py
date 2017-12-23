# 生成给定长度的合法括号串. 用回溯的方法, 当左边
# 还能放, 就使劲放, 放够了就放右边, 注意右边的值
# 不能大于左边, 当右边的值等于给定长度时, 输出

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(temp, left, right):
            if right == n:
                result.append(temp)
            else:
                if left < n:
                    backtrack(temp+'(', left+1, right)
                if right < left:
                    backtrack(temp+')', left, right+1)

        backtrack('', 0, 0)
        return result

print(Solution().generateParenthesis(3))