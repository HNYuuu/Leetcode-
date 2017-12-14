class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # @param temp: list
        def isPalindrome(temp):
            length = len(temp)
            back = []
            if length % 2 == 0:
                back = temp[length - 1:length // 2 - 1:-1]
            else:
                back = temp[length - 1:length // 2:-1]
            if back == temp[:length // 2]:
                return True
            else:
                return False

        temp = [i for i in s]
        if isPalindrome(temp):
            return True
        i, j = 0, len(temp)-1
        while i != j:
            if temp[i] == temp[j]:
                i += 1
                j -= 1
            else:
                tempPop = temp.pop(i)
                if isPalindrome(temp):
                    return True
                temp.insert(i, tempPop)
                tempPop = temp.pop(j)
                if isPalindrome(temp):
                    return True
                return False


print(Solution().validPalindrome('abcfba'))
