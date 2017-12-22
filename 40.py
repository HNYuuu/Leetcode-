# 从一个给定数组中寻找和是 target 的一个组合. 昨天那道题的
# 进化版, 要求是一个元素不能用多次, 所以新增了一个 popout 
# 变量, 用来记录弹出的值, 如果下一个要添加的值和刚刚弹出的
# 值一样, 那么就没有什么意义, 而且结果数组中还会出现重复

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        candidates.reverse()
        result = []

        def backtrack(temp, start):
            if sum(temp) == target:
                result.append(temp.copy())
            elif sum(temp) < target:
                popout = float('inf')
                for i in range(start, len(candidates)):
                    if candidates[i] != popout:
                        temp.append(candidates[i])
                        backtrack(temp, i+1)
                        popout = temp.pop()
                    else:
                        continue
        
        backtrack([], 0)
        return result

print(Solution().combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 2))