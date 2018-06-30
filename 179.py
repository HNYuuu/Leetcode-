class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        nums.sort(reverse=True)
        return nums

print(Solution().largestNumber([3,30,34,5,9]))