class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle == '':
            return 0
        self.nextList = [0]*(len(needle))

        def getNext(s, nextList):
            length = len(s)
            k = -1
            j = 0
            self.nextList[0] = -1
            while j < length-1:
                if k == -1 or s[j] == s[k]:
                    k += 1
                    j += 1
                    if s[j] != s[k]:
                        self.nextList[j] = k
                    else:
                        self.nextList[j] = self.nextList[k]
                else:
                    k = self.nextList[k]
        
        getNext(needle, self.nextList)

        i, j = 0, 0
        sLen, pLen = len(haystack), len(needle)
        while i < sLen and j < pLen:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = self.nextList[j]
        if j == pLen:
            return i-j
        else:
            return -1

print(Solution().strStr('mississippi', 'issip'))