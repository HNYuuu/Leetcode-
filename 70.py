class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = [0 for x in range(n+1)]
        self.cache[1] = 1
        self.cache[0] = 1

        def calc(n):
            if n == 1 or n == 0:
                return 1
            if self.cache[n] == 0:
                self.cache[n] = calc(n-1) + calc(n-2)
            return self.cache[n]

        result = calc(n)
        return result

print(Solution().climbStairs(100))

