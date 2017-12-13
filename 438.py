class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        def s2d(s):
            temp = {}
            for i in s:
                if i not in temp.keys():
                    temp[i] = 1
                else:
                    temp[i] += 1
            return temp

        standard = s2d(p)
        temp = s2d(s[0:len(p)])
        result = []
        if temp == standard:
            result.append(0)

        i = 1
        while i <= len(s)-len(p):
            if 1 == temp[s[i-1]]:
                temp.pop(s[i-1])
            else:
                temp[s[i-1]] -= 1
            
            if s[i+len(p)-1] not in temp.keys():
                temp[s[i+len(p)-1]] = 1
            else:
                temp[s[i+len(p)-1]] += 1

            if temp == standard:
                result.append(i)
            
            i += 1

        return result

print(Solution().findAnagrams('ababbaababa', 'abab'))