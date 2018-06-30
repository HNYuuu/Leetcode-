class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lol
        # return min(nums)

        l, r = 0, len(nums)-1

        while r-l>1:
            m = l+(r-l)//2
            if nums[r] < nums[l]:
                if nums[m] > nums[r]:
                    l = m
                else:
                    r = m
            else:
                r = m

        return min(nums[l], nums[r])

print(Solution().findMin([3,4,5,6]))