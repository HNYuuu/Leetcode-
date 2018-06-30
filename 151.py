class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.strip()
        words = s.split()
        words.reverse()
        return ' '.join(words)

print(Solution().reverseWords("the sky is blue"))