class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        def backtrack(permutation, l, r):
            if l == r:
                result.add(tuple(permutation))
            else:
                for i in range(l, r):
                    if i == l or (i != l and permutation[i] != permutation[l]):
                        permutation[i], permutation[l] = permutation[l], permutation[i]
                        backtrack(permutation, l+1, r)
                        permutation[i], permutation[l] = permutation[l], permutation[i]

        backtrack(nums, 0, len(nums))
        return [list(i) for i in result]

print(Solution().permuteUnique([1,1,2,2]))