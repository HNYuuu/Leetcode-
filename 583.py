# 计算两个字符串的编辑距离, 但是只有删除操作. 这道题和之
# 前做过的一道很像, 思路都是 DP, 记住如果已经计算过直接
# 取值, 不要再算一遍, 不然 DP 没有意义

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cache = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(word2)+1):
            cache[0][i] = i
        for j in range(len(word1)+1):
            cache[j][0] = j

        def diff(i, j):
            return 0 if word1[i-1] == word2[j-1] else 2

        def dp(i, j):
            if i == 0 or j == 0:
                return cache[i][j]
            else:
                if word1[i-1] != word2[j-1]:
                    temp1 = cache[i-1][j] if cache[i-1][j] != 0 else dp(i-1, j)
                    temp2 = cache[i][j-1] if cache[i][j-1] != 0 else dp(i, j-1)
                    cache[i][j] = min(temp1+1, temp2+1)
                else:
                    temp = cache[i-1][j-1] if cache[i-1][j-1] != 0 else dp(i-1, j-1)
                    cache[i][j] = dp(i-1, j-1)
                return cache[i][j]

        dp(len(word1), len(word2))
        return cache[len(word1)][len(word2)]

print(Solution().minDistance("dinitrophenylhydrazine",
"benzalphenylhydrazone"))