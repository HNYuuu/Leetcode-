# 找到一个list中两个只出现了一次的元素，限制：O(n)、Ω(1)。
# 具体代码注释

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        remainTwo = 0
        # 先所有异或一遍，这样remainTwo至少有一位不为零
        for num in nums:
            remainTwo ^= num
        # 找到最右边的不为零的那一位
        remainTwo &= -remainTwo

        num1, num2 = 0, 0

        for num in nums:
            # 将list分为两组，一组是与运算后为0，另一组
            # 不为零，因为那两个不一样的值正好这一位不一
            # 样，所以会被分到两个数组中去，这样可以通过
            # 异或的方法找出来
            if remainTwo & num == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

print(Solution().singleNumber([1,1,3,7,2,2,4,4]))