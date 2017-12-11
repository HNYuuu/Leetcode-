class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, maximum, cur_max = 0, 0, 0
        while i < len(nums):
            cur = nums[i]
            if cur_max+cur < 0:
                cur_max = 0
            else:
                cur_max += nums[i]
                if cur_max > maximum:
                    maximum = cur_max
            i += 1
        if maximum > 0:
            return maximum
        else:
            return max(nums)

print(Solution().maxSubArray([8,-19,5,-4,20]))