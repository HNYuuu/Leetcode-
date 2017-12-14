class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = list(filter(lambda x: x.isalnum(), s.lower()))
        if len(temp) == 0:
            return True
        length = len(temp)
        back = []
        if length%2 == 0:
            back = temp[length-1:length//2-1:-1]
        else:
            back = temp[length-1:length//2:-1]
        if back == temp[:length//2]:
            return True
        else:
            return False

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))