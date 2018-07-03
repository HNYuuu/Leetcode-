class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        for j in range(1, len(nums) + 1):
            if sum(nums[:j]) >= s:
                break
        # not found such j
        if sum(nums[:j]) < s:
            return 0

        now_min = j
        i = 0
        now_sum = sum(nums[i:j])
        while j <= len(nums):
            if now_sum >= s:
                i += 1
                now_sum -= nums[i-1]
                if now_sum >= s and j - i < now_min:
                    now_min = j - i
            else:
                j += 1
                if j > len(nums):
                    break
                now_sum += nums[j-1]

        return now_min

        # except this solution, you can sort the nums and from the biggest element side to find the min length
