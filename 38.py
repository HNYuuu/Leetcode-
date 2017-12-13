class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        s = '1'
        while i < n:
            end = 0
            cur = s[end]
            count = 0
            result = []
            while end < len(s):
                if s[end] == cur:
                    count += 1
                    end += 1
                    continue
                else:
                    result.append(str(count))
                    result.append(cur)
                    cur = s[end]
                    count = 0
            result.append(str(count))
            result.append(cur)
            s = "".join(result)
            i += 1
        return s

print(Solution().countAndSay(4))