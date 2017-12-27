# 抢劫的升级版, 变成了一个环形, 所以头尾也要判断一次. 
# 因此第一次抢是除掉第一个, 第二次是除掉最后一个, 返
# 回这两个的最大值

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[2], nums[1])

        def dp(n):
            if cache[n-1] != -1:
                temp1 = cache[n-1]
            else:
                temp1 = dp(n-1)
                cache[n-1] = temp1
            if cache[n-2] != -1:
                temp2 = cache[n-2]
            else:
                temp2 = dp(n-2)
                cache[n-2] = temp2
            return max(temp1, temp2+nums[n])
        
        
        cache = [-1]*len(nums)
        cache[0] = nums[1]
        cache[1] = max(nums[1], nums[2])
        temp = nums.pop(0)
        r1 = dp(len(nums)-1)

        nums.insert(0, temp)
        nums.pop()
        cache = [-1]*len(nums)
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        r2 = dp(len(nums)-1)

        return max(r1, r2)

print(Solution().rob([1,1,1]))