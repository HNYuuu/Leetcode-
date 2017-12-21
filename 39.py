# 找到一个数组中可以凑成目标树的所有组合, 元素可以重复. 
# 用回溯法, 先把所有的给定元素从大到小排序, 然后一个个
# 遍历, 如果小于目标值, 那么加一个, 递归

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates, reverse=True)
        result = []
        temp = []

        def backtrack(temp, start):
            if sum(temp) == target:
                result.append(temp.copy())
            elif sum(temp) < target:
                for i in range(start, len(candidates)):
                    temp.append(candidates[i])
                    backtrack(temp, i)
                    temp.pop()
            else:
                return
        
        backtrack([], 0)
        return result

print(Solution().combinationSum([2,3,6,7], 7))