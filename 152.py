import functools


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp solution
        # TLE
        # result = [[-2 ** 32 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     result[i][i + 1] = nums[i]
        #
        # def dp(i, j):
        #     if result[i][j] != -2**32:
        #         return result[i][j]
        #     elif j == i + 2:
        #         a = nums[i]
        #         b = nums[i + 1]
        #         result[i][j] = a * b if a * b > 0 else max(a, b)
        #         return result[i][j]
        #     else:
        #         result[i][j] = max(dp(i + 1, j), dp(i, j - 1), functools.reduce(lambda x, y: x * y, nums[i:j]))
        #         return result[i][j]
        #
        # return dp(0, len(nums))

        max_so_far = nums[0]
        max_end = nums[0]
        min_end = nums[0]

        for i in range(1, len(nums)):
            temp = max_end
            max_end = max(max_end*nums[i], min_end*nums[i], nums[i])
            min_end = min(temp*nums[i], min_end*nums[i], nums[i])
            if max_so_far < max_end:
                max_so_far = max_end

        return max_so_far


print(Solution().maxProduct([2,3,-2,4]))
