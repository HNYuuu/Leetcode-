# 从1-9找到 k 个数, 使得其和为 n. 还是和前面的思路一样, 
# 只不过改成了自定义 candidates = [9,8,7,6,5,4,3,2,1], 
# 在回溯的时候判断一下当前数组长度即可

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [9,8,7,6,5,4,3,2,1]
        result = []

        def backtrack(temp, start):
            if len(temp) > k:
                return
            if sum(temp) == n:
                if len(temp) == k: 
                    result.append(temp.copy())
                else:
                    return
            elif sum(temp) < n:
                for i in range(start, len(candidates)):
                    temp.append(candidates[i])
                    backtrack(temp, i+1)
                    temp.pop()
        
        backtrack([], 0)
        return result

print(Solution().combinationSum3(3,9))