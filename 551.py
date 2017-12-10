class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        for i in range(len(s)):
            if s[i] == 'L' and i+1 < len(s) and s[i+1] == 'L' and i+2 < len(s) and s[i+2] == 'L':
                return False
        return True

print(Solution().checkRecord('PPALLPLLPLLLPLL'))
