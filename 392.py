# 给定两个字符串, 判定是否是子串. 用 find 函数, 
# 给定起始值是上次找到的地方加一, 如果没找到返回 
# False, 如果全找完了返回 True

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0

        for i in range(len(s)):
            j = t.find(s[i], j) + 1
            if j == 0:
                return False
        return True

print(Solution().isSubsequence("leeeeetcode",
"laskdfjgfhdgsawesgdfhfsgaerfd"))