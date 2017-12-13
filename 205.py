class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.sdict, self.tdict = {}, {}
        
        def s2d(s, sdict):
            i = 0
            while i < len(s):
                if s[i] not in sdict.keys():
                    sdict[s[i]] = [i]
                else:
                    sdict[s[i]].append(i)
                i += 1
        
        s2d(s, self.sdict)
        s2d(t, self.tdict)
        for i in self.sdict.values():
            if i not in self.tdict.values():
                return False
        return True

print(Solution().isIsomorphic('', ''))

