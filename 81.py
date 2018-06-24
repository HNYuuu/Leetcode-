class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        l, r = 0, len(nums) - 1

        while r - l > 1:
            m = l + (r - l) // 2
            # right sorted
            if nums[m] < nums[r]:
                if nums[r] >= target >= nums[m]:
                    l = m
                else:
                    r = m
            # left side sorted
            elif nums[m] > nums[r]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m
            else:
                r -= 1
        if nums[l] == target or nums[r] == target:
            return True
        else:
            return False

print(Solution().search([2,5,6,0,0,1,2],1))