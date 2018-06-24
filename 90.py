class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        nums.sort()

        def backtrack(t, data):
            if t == len(nums):
                result.add(tuple(data))
            else:
                for i in [0,1]:
                    if i == 1: data.append(nums[t])
                    backtrack(t+1, data)
                    if i == 1: data.pop()

        backtrack(0, [])
        return [list(e) for e in result]

print(Solution().subsetsWithDup([]))