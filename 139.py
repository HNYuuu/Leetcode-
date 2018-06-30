class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # TLE
        # if len(wordDict) == 0:
        #     return False
        # wordDict = set(wordDict)
        # max_len = len(max(wordDict, key=len))
        #
        # got_it = [False]
        #
        # def backtrack(i):
        #     if i == len(s):
        #         got_it[0] = True
        #     else:
        #         for j in range(min(i+max_len, len(s)), i, -1):
        #             if s[i:j] in wordDict:
        #                 backtrack(j)
        #                 if got_it[0]:
        #                     return
        #
        # backtrack(0)
        #
        # return got_it[0]

        result = [False for _ in range(len(s)+1)]
        result[0] = True

        for i in range(len(s)+1):
            if not result[i]:
                continue
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    result[i+len(word)] = True

        return result[len(s)]



print(Solution().wordBreak('applepenapple', ['apple', 'pen']))