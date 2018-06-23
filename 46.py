class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(permutation, l, r):
            if l == r:
                result.append(permutation.copy())
            else:
                for i in range(l, r+1):
                    permutation[i], permutation[l] = permutation[l], permutation[i]
                    backtrack(permutation, l+1, r)
                    permutation[i], permutation[l] = permutation[l], permutation[i]
            
        backtrack(nums, 0, len(nums)-1)
        return result

print(Solution().permute([1,1,5]))