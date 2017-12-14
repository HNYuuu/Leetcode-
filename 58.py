class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s.rstrip()

        count, i = 0, len(t)-1
        while i >= 0:
            if not t[i].isspace():
                count += 1
                i -= 1
            else:
                break
        return count

print(Solution().lengthOfLastWord('hello, world  '))

