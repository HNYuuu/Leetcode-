# 给定两个操作, 复制所有以及粘贴, 对于每一个给定
# 的n, 有递推方程 F(n) = min(F(j) + n//j) 
# 其中 j < n 并且 j 是 n 的因子

import math

class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def getFactors(n):
            result = []
            for i in range(1, math.ceil(math.sqrt(n))+1):
                if n%i == 0:
                    result.append(i)
                    result.append(n//i)
            return result

        cache = [float('inf')] * (n+1)
        cache[1] = 0

        for i in range(2, n+1):
            factors = getFactors(i)
            for j in factors:
                cache[i] = min(cache[i], cache[j]+i//j)
        return cache[n]

print(Solution().minSteps(1000))
