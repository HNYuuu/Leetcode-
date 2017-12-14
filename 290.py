class Solution:
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        plist = [i for i in pattern]
        slist = string.split(' ')
        if len(plist) != len(slist):
            return False

        jection = {}
        reverse = {}
        i = 0
        while i < len(plist):
            a = plist[i]
            b = slist[i]
            if a not in jection.keys() and b not in reverse.keys():
                jection[a] = b
                reverse[b] = a
            elif a in jection.keys() and b in reverse.keys():
                if jection[a] != b or reverse[b] != a:
                    return False
            else:
                return False
            i += 1
        return True




print(Solution().wordPattern("abc", "c b a"))