class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(A[0]) == 0:
            return [[]]
        return [list(x) for x in list(zip(*A))]

print(Solution().transpose([[1]]))