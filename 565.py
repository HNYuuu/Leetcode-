# 找一个数组中头尾相连的链的最大元素个数。从 0 开始
# 遍历，没遍历一个就置为 -1，直到一个链遍历结束，和
# 当前最大值比较。随后再遍历下一个非 -1 元素 O(n) 
# Ω(1)

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        maximum = 0
        while i < len(nums):
            if nums[i] == -1:
                i += 1
                continue
            start = nums[i]
            count = 1
            nums[i] = -1
            while nums[start] != nums[i]:
                count += 1
                temp = start
                start = nums[start]
                nums[temp] = -1
            maximum = max(maximum, count)
            i += 1
        return maximum

print(Solution().arrayNesting([0,2,1]))