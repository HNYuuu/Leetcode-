class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = len(nums)-1
        while True:
            while left < len(nums) and nums[left] != val:
                left += 1
            if left > right:
                break
            else:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                right -= 1
                length -= 1
        return length

print(Solution().removeElement([1,2,3,2,2,3,4], 0))
