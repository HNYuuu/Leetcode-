class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsCache = nums.copy()
        nums.sort()
        i = 0
        while i < len(nums):
            numsCache[i] -= nums[i]
            i += 1
        i, j = 0, len(nums)-1
        while i <= j and numsCache[i] == 0:
            i += 1
        if i > j:
            return 0
        while numsCache[j] == 0:
            j -= 1
        return j-i+1
            
        