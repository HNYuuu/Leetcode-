class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # TLE
        # but it can pass some test case
        # nums.insert(0, 0)
        # if sum(nums) % 2 == 1:
        #     return False
        # dp = [[-2**32 for _ in range(sum(nums)//2+1)] for _ in range(len(nums))]
        #
        # for i in range(len(nums)):
        #     dp[i][0] = 0
        # for j in range(len(dp[0])):
        #     dp[0][j] = 0
        #
        # for i in range(1, len(nums)):
        #     for j in range(sum(nums)//2 + 1):
        #         if j < nums[i]:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])
        #
        # return dp[-1][-1] == sum(nums)//2

        nums.insert(0, 0)
        my_sum = sum(nums)
        if my_sum % 2 == 1:
            return False
        dp = [-2**32 for _ in range(my_sum//2 + 1)]
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(my_sum//2, nums[i]-1, -1):
                dp[j] = dp[j] if dp[j]>dp[j-nums[i]]+nums[i] else dp[j-nums[i]]+nums[i]
            if dp[-1] == my_sum//2:
                return True

        return False

print(Solution().canPartition([81,70,90,44,47,61,41,36,94,37,69,50,41,32,17,87,75,86,10,23,22,48,8,80,98,17,11,48,46,41,26,35,81,95,69,16,58,82,14,6,50,77,26,32,78,60,71,10,100,81,8,29,16,67,38,87,33,77,41,65,27,45,46,39,69,100,44,29,25,91,46,53,85,54,40,43,9,79,15,35,53,88,45,4,67,38,15,18,99,3,3,100,70,6,23,100,52,62,3,37]))