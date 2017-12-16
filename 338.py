# 给定一个数字，计算不大于它的所有的数字的二进制的比特一的个数。用DP的
# 思想，首先初始化一个数组全部为-1，只有0为0，然后观察有没有递推式，发
# 现：如果一个数是偶数，它的比特一的个数就是它除以二的那个数的个数；如
# 果是奇数，就是比它小一的那个数的个数加一；边界条件就是0的个数为0 。

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        self.cache = [-1] * (num+1)
        self.cache[0] = 0

        def calcBits(num):
            if num == 0:
                return 0
            if num%2 == 0:
                if self.cache[num//2] != -1:
                    self.cache[num] = self.cache[num//2]
                else:
                    self.cache[num] = calcBits(num//2)
                return self.cache[num]
            else:
                if self.cache[num-1] != -1:
                    self.cache[num] = self.cache[num-1]+1
                else:
                    self.cache[num] = calcBits(num-1)+1
                return self.cache[num]

        for i in range(1, num+1):
            calcBits(i)
        return self.cache

print(Solution().countBits(100))