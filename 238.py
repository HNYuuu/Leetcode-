# 给定一个 list，求一个 list 使得对应位置的值为其余元素的乘积，
# 限制 O(n)，不用除法。记录一个左边乘积数组，再记录一个右边乘积
# 数组，最后的结果就是这两个数组按位相乘

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProduct = [1] * len(nums)
        rightProduct = [1] * len(nums)

        i = 1
        while i < len(nums):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
            i += 1
        
        j = len(nums)-2
        while j >= 0:
            rightProduct[j] = rightProduct[j+1] * nums[j+1]
            j -= 1
        
        output = [1] * len(nums)
        i = 0
        while i < len(nums):
            output[i] = leftProduct[i] * rightProduct[i]
            i += 1
        return output

print(Solution().productExceptSelf([1,2,3,0,5,6]))