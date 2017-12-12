class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = s+s
        sub = s1[1:-1]
        if s in sub:
            return True
        else:
            return False

print(Solution().repeatedSubstringPattern('abab'))