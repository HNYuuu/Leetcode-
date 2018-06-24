class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1,n+1)]
        result = []

        def backtrack(i, data):
            if len(data) == k:
                result.append(data.copy())
            else:
                for j in range(i+1, len(nums)):
                    data.append(nums[j])
                    backtrack(j, data)
                    data.pop()

        backtrack(-1, [])
        return result


print(Solution().combine(6,5))