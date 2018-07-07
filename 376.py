from itertools import groupby

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        # remove the consecutive duplicated elements
        nums = [k for k,g in groupby(nums)]
        if len(nums) <= 1:
            return len(nums)

        diff = []

        for i in range(1, len(nums)):
            diff.append((nums[i]-nums[i-1])>0)

        return len([k for k, g in groupby(diff)])+1



print(Solution().wiggleMaxLength([1,1,1,1,1,1,1]))