class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = {}
        i = 0
        while i < len(nums):
            if nums[i] not in temp.keys():
                temp[nums[i]] = i
            else:
                index = temp[nums[i]]
                if i - index <= k:
                    return True
                temp[nums[i]] = i
            i += 1
        return False

print(Solution().containsNearbyDuplicate([1,2,3,1,4], 3))