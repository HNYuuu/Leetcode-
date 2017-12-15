class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        ascNum = 0
        index = []
        i = 0
        while i < len(nums)-1:
            if nums[i+1] >= nums[i]:
                i += 1
            else:
                ascNum += 1
                index.append(i)
                i += 1
        ascNum += 1
        if ascNum == 1:
            return True
        elif ascNum >= 3:
            return False
        else:
            if index[0] == 0 or index[0] == len(nums)-2:
                return True
            else:
                if index[0]+2 < len(nums) and nums[index[0]+2] >= nums[index[0]]:
                    return True
                if nums[index[0]+1] >= nums[index[0]-1]:
                    return True
                else:
                    return False

print(Solution().checkPossibility([1,2,4,5,3]))