class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cache = [0]*(len(nums)-k+1)
        for i in range(len(cache)):
            if i == 0:
                cache[0] = sum(nums[0:k])
            else:
                cache[i] = cache[i-1]+nums[i-1+k]-nums[i-1]
        return max(cache)/k

print(Solution().findMaxAverage([1,12,-5,-6,50,3],4))
