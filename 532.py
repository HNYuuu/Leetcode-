class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k > 0:
            temp = {i for i in nums}
            result = 0
            for i in temp:
                if i+k in temp:
                    result += 1
            return result
        else:
            result = 0
            temp = set()
            cache = set()
            for i in nums:
                if i not in temp:
                    temp.add(i)
                elif i not in cache:
                    result += 1
                    cache.add(i)
            return result

print(Solution().findPairs([3,1,4,1,5], 2))