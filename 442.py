# 寻找一个给定数组的所有重复出现了两次的值，要求时间复杂度O(n)不用
# 额外空间。其实本身不是一道难题，用各种各样的数据结构都可以轻松的
# 做出来。但是要求不用额外空间很难受，本来打算用bit flag但是这也
# 算是一种和长度相关的hash表，不能用。看了一下高票答案的思路发现
# 将对应的位翻转，当发现该位已经为负数时，这个就是重复的值。差一点
# 就想到了

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        while i < len(nums):
            index = nums[i]*(-1) if nums[i]<0 else nums[i]
            if nums[index-1] < 0:
                result.append(index)
            else:
                nums[index-1] *= -1
            i += 1
        return result

print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))

