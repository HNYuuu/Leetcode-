class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumArray = []
        total = 0
        for i in nums:
            total += i
            sumArray.append(total)
        i = 0
        while i < len(nums):
            if i == 0:
                if sumArray[len(nums)-1]-sumArray[i] == 0:
                    return 0
            else:
                if sumArray[i-1] == sumArray[len(nums)-1]-sumArray[i]:
                    return i
            i += 1
        return -1

print(Solution().pivotIndex([0]))