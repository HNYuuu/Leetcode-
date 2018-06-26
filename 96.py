class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [-1 for _ in range(n+1)]
        result[0] = 1
        result[1] = 1

        def dp(i):
            if result[i] != -1:
                return result[i]
            else:
                temp = 0
                for k in range(i):
                    temp += (dp(k) * dp(i-1-k))
                result[i] = temp
                return result[i]

        dp(n)
        return result[-1]

print(Solution().numTrees(1))