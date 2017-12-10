class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        i = 0
        tempLength = 1
        maximum = 1
        while i < len(nums):
            if i+1 < len(nums) and nums[i] < nums[i+1]:
                tempLength += 1
                i += 1
                continue
            maximum = max(maximum, tempLength)
            i += 1
            tempLength = 1
        return maximum

print(Solution().findLengthOfLCIS([2,2,2,2,2]))
