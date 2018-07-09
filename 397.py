class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 1:
            if n == 3:
                count += 2
                break
            if n%2 == 0:
                n >>= 1
            else:
                more = bin(n+1)[2:]
                less = bin(n-1)[2:]
                less.zfill(len(more))
                if more.count('1') > less.count('1'):
                    n -= 1
                else:
                    n += 1
            count += 1
        return count

print(Solution().integerReplacement(100000000))