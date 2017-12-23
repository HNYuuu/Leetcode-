# 给定一个整数, 将其分解为至少两个整数, 求其乘积的最大值. 
# 这道题用 DP, 每一个 n 可以表示为 x * F(n-x), 这样就
# 表示了所有分解为三个及以上的情况, 再加一个 n//2 * n-n//2 
# 这个分解为两个数的情况, 取最大值即可

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [1] * 60

        for i in range(3, n+1):
            temp = []
            for j in range(1, i):
                temp.append(j*cache[i-j])
            temp.append((i//2)*(i-(i//2)))
            cache[i] = max(temp)
        
        return cache[n]

print(Solution().integerBreak(58))