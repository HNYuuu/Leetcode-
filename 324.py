from math import ceil

class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # time: O(nlogn)
        # space: O(n)
        tmp = nums.copy()
        tmp.sort()
        last, mid = len(nums)-1, ceil(len(nums)/2)-1

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = tmp[mid]
                mid -= 1
            else:
                nums[i] = tmp[last]
                last -= 1
        return nums

print(Solution().wiggleSort([]))