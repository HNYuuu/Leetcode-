class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        end = 0
        cur = nums[end]
        count = 0
        while end < len(nums):
            if nums[end] == cur:
                count += 1
                if count > 1:
                    nums.pop(end)
                    continue
                end += 1
            else:
                cur = nums[end]
                count = 0
        return len(nums)

print(Solution().removeDuplicates([1,1,2,2,2,2,2,3,3,3,3]))