class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums.copy()
        temp.sort()
        if temp[-1] >= 2*temp[-2]:
            return nums.index(temp[-1])
        else:
            return -1

print(Solution().dominantIndex([1,6,3,0]))