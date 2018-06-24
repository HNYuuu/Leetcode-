class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0

        store = [-1 for _ in range(len(s)+1)]
        store[0], store[1] = 1, 1

        def count(n):
            if store[n] != -1:
                return store[n]

            time = 0
            if s[n-1] != '0':
                time = count(n-1)
            if s[n-2] == '1' or (s[n-2] == '2' and int(s[n-1]) <= 6):
                time += count(n-2)
            store[n] = time
            return store[n]

        count(len(s))
        return store[-1]

print(Solution().numDecodings("408539358726343819"))