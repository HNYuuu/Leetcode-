# 有一个list，只有一个元素出现了一次剩下的都是两次，找到
# 那个值。限制：时间复杂度O(logn)，空间复杂度O(1)。本
# 来是可以用位操作的，把所有的异或一次就可以找到，但是
# O(n)不符合要求，于是想到了二分。这分为两种情况：如果中
# 间值的左右两边的个数是偶数个，那么中间值和左值相等时搜
# 左边；奇数的话反过来。其实说白了就是一个找规律的题

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        m = (r-l)//2+l
        while l < r:
            if m-1 >= 0 and nums[m] != nums[m-1] and m+1 <= len(nums)-1 and nums[m] != nums[m+1]:
                return nums[m]
            if (r-m)%2 == 0:
                if nums[m] == nums[m-1]:
                    r = m
                else:
                    l = m
            else:
                if nums[m] == nums[m-1]:
                    l = m+1
                else:
                    r = m-1
            m = (r-l)//2+l
        return nums[m]

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,5,5]))
