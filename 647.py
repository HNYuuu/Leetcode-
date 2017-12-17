# 计算所有回文子串的个数。用dp的思想，从i到j是不是回文串取决于
# s[i] == s[j-1]以及从i+1到j-1是不是一个回文串。一定要掌握
# 好dp函数内部的实现，一开始TLE是因为我的dp完全没有搜表，每一
# 次都是重新赋值，所以就相当于暴力了，后面加了搜表的操作就AC了

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cache = [[False for j in range(0, len(s)+1)] for i in range(0, len(s))]

        def dp(s, i, j):
            if self.cache[i][j] == True:
                return True
            if j == i+1:
                self.cache[i][j] = True
                return True
            elif j == i+2:
                if s[i] == s[j-1]:
                    self.cache[i][j] = True
                    return True
                else:
                    return False
            else:
                self.cache[i][j] = True if s[i] == s[j-1] and dp(s, i+1, j-1) else False
                return self.cache[i][j]

        length = len(s)
        for l in range(1, length+1):
            for i in range(0, length-l+1):
                j = i+l
                dp(s, i, j)
        
        count = 0
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                if self.cache[i][j] == True:
                    count += 1
        return count

print(Solution().countSubstrings("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))