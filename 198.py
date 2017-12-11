class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        self.result = [-1 for x in range(total+1)]
        
        def money(x):
            if x == 0:
                return 0
            elif x == 1:
                return nums[0]
            elif x == 2:
                return max(nums[0], nums[1])
            else:
                if self.result[x] == -1:
                    self.result[x] = max(nums[x-1]+money(x-2), nums[x-2]+money(x-3))
                return self.result[x]

        return money(total)

print(Solution().rob([1,2,3,4,5,6,7]))
        