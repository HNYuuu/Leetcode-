class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if len(nums) == 0:
            return 0
        elif min(nums) > target:
            return 0
        store = [0 for _ in range(target+1)]
        store[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    store[i] += store[i-num]
                else:
                    continue

        return store[target]



print(Solution().combinationSum4([1,2,3] ,1000))