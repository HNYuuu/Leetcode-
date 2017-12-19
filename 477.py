class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # if len(nums) <= 1:
        #     return 0

        # maximum = 0
        # for num in nums:
        #     maximum = max(maximum, len(bin(num)[2:]))
        
        # cache = [0] * maximum
        # for num in nums:
        #     for j in range(0, maximum):
        #         temp = bin(num)[2:].zfill(maximum)
        #         if temp[j] == '1':
        #             cache[j] += 1

        # result = 0
        # for i in cache:
        #     result += i*(len(nums)-i)
        # return result

        # Solution 2
        # More fast and save space
        bitCnt = 0
        result = 0
        for i in range(0, 32):
            for num in nums:
                bitCnt += (num >> i) & 1
            result += bitCnt*(len(nums)-bitCnt)
            bitCnt = 0
        return result

print(Solution().totalHammingDistance([4,14,2,8,10,12]))
