class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = set()
        duplicate = 0
        length = len(nums)
        ordinary = (1+length)*length//2
        now = sum(nums)
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                duplicate = i
                break
        return [duplicate, duplicate+(ordinary-now)]

print(Solution().findErrorNums([1,2,2,3]))