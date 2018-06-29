class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in nums:
            b = (b ^ i) & (~a)
            a = (a ^ i) & (~b)
        return b

print(Solution().singleNumber([2,2,3,2,1,1,1]))
