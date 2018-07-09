class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # divide and conquer
        counter = {}
        for c in s:
            counter[c] = 1 if c not in counter.keys() else 1+counter[c]

        flags = [-1]
        for c in range(len(s)):
            if counter[s[c]] < k:
                flags.append(c)

        # if every char has appeared more than k times
        # you should return current length
        if len(flags) == 1:
            return len(s)
        else:
            flags.append(len(s))

        my_max = 0
        for i in range(len(flags)-1):
            temp_max = self.longestSubstring(s[flags[i]+1:flags[i+1]], k)
            if temp_max > my_max:
                my_max = temp_max

        return my_max

print(Solution().longestSubstring("aaabb",3))