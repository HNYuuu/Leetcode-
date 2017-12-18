# 给定一个list，求一点令所有点到这一点的和最小。一开始用了方差公式求
# 最小值，求出来是平均数，但是 WA 了一次。然后发现是求对中位数的差，
# 这里要分情况：奇数的话，那么左边到中间的差值为 x，右边到中间的差值
# 为 y，如果不是中位数，比如说向左移了一个，那么左边和右边的减少和增
# 加会抵消，但是原来的中间值还会产生一个正值，比原来的大；偶数的话，
# 取中间两数的平均值，以及它们两个分别计算一次公式，发现是相等的，右
# 半部分减左半部分即可

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) % 2 == 0:
            return sum(nums[len(nums)//2:]) - sum(nums[:len(nums)//2])
        else:
            return sum(nums[len(nums)//2+1:]) - sum(nums[:len(nums)//2])

print(Solution().minMoves2([1,2,3,4]))

