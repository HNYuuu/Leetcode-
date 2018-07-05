class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        i,j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return nums[i]
            i += 1
            j += 1

print(Solution().findDuplicate([1,3,4,2,2]))