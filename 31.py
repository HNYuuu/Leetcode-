class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            pass
        else:
            do_it = False
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    min_val = min([e for e in nums[i + 1:] if e > nums[i]])
                    min_i = nums.index(min_val, i+1)
                    nums[i], nums[min_i] = nums[min_i], nums[i]
                    nums[i+1:] = sorted(nums[i+1:])
                    do_it = True
                    break
            if not do_it:
                nums.reverse()

Solution().nextPermutation([5,4,7,5,3,2])