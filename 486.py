# 每一次只能从两头拿数字, 问A可不可以拿的比B多. 用DP, 
# 将题目转换为A拿一个为正数, B拿一个为负数, 这样计算差
# 值是否大于等于零即可, 因此可以构造方程. 一开始想用纯
# 递归做, 但是TLE了, 所以加上了一个cache数组用来计算
# 从i到j的可以拿到的最大值, AC

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        cache = [[-1 for i in range(len(nums))] for j in range(len(nums))]
        
        def diff(start, end):
            if end == start + 1:
                cache[start][end] = nums[end]-nums[start] if nums[end]>nums[start] else nums[start]-nums[end]
                return cache[start][end]
            else:
                if cache[start+1][end] != -1:
                    temp1 = cache[start+1][end]
                else:
                    temp1 = diff(start+1, end)
                    cache[start+1][end] = temp1
                
                if cache[start][end-1] != -1:
                    temp2 = cache[start][end-1]
                else:
                    temp2 = diff(start, end-1)
                    cache[start][end-1] = temp2
                return max(nums[start]-temp1, nums[end]-temp2)

        result = diff(0, len(nums)-1)
        return True if result >= 0 else False

print(Solution().PredictTheWinner([0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]))