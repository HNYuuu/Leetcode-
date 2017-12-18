# 给定两个字符串，找到一个 LCS 使得两个字符串的ascii和减去 LCS 的 ascii 和最小。
# 思路一：使用 DP 找到所有的 LCS，对每个 LCS 计算 ascii 差，返回最小的，果不其然
#  TLE了；思路二：上网查了一下发现这道题是编辑距离的特例，只能删除，不能替换，因此
#  可以构造 DP 表，每一个 dp[i][j] 就是当前所能构造出来的最小 ascii 和，但是 
#  Python 跑的有点慢，C++可以 AC ，Python在最后几个大数据 TLE；思路三：构造一
#  个特殊的 DP 表，里面存的是当前最大 ascii 公共子序列的值，这样最后用 s1 和 s2 
#  的和减去二倍右下角的值即可，终于 AC

class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # Solution 1: TLE
        # self.dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

        # # Use DP to get the length table
        # i = 1
        # while i <= len(s1):
        #     j = 1
        #     while j <= len(s2):
        #         if s1[i-1] == s2[j-1]:
        #             self.dp[i][j] = self.dp[i-1][j-1] + 1
        #         else:
        #             self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])
        #         j += 1
        #     i += 1

        # # Use iteration to get all LCS
        # self.LCSS = set()
        # def traceback(i, j, tempstr):
        #     while i > 0 and j > 0:
        #         if s1[i-1] == s2[j-1]:
        #             tempstr = s1[i-1] + tempstr
        #             i -= 1
        #             j -= 1
        #         elif self.dp[i-1][j] > self.dp[i][j-1]:
        #             i -= 1
        #         elif self.dp[i-1][j] < self.dp[i][j-1]:
        #             j -= 1
        #         else:
        #             traceback(i-1, j, tempstr)
        #             traceback(i, j-1, tempstr)
        #             return
        #     self.LCSS.add(tempstr)
        
        # traceback(i-1, j-1, '')

        # # Calculate the min ascii sum
        # sums1 = sum([ord(i) for i in s1])
        # sums2 = sum([ord(i) for i in s2])
        # minimum = float('inf')
        # for lcs in self.LCSS:
        #     sumlcs = sum([ord(i) for i in lcs])
        #     tempResult = sums1 + sums2 - 2*sumlcs
        #     if tempResult < minimum:
        #         minimum = tempResult
        # return minimum

        # Solution 2
        # Nearly AC, TLE, however
        # Construct the DP table
        # self.dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        # j = 1
        # while j <= len(s2):
        #     self.dp[0][j] = self.dp[0][j-1] + ord(s2[j-1])
        #     j += 1
        # i = 1
        # while i <= len(s1):
        #     self.dp[i][0] = self.dp[i-1][0] + ord(s1[i-1])
        #     i += 1

        # def diff(i, j):
        #     return ord(s1[i-1])+ord(s2[j-1]) if s1[i-1] != s2[j-1] else 0

        # i = 1
        # while i <= len(s1):
        #     j = 1
        #     while j <= len(s2):
        #         self.dp[i][j] = min(self.dp[i-1][j]+ord(s1[i-1]), self.dp[i][j-1]+ord(s2[j-1]), self.dp[i-1][j-1]+diff(i, j))
        #         j += 1
        #     i += 1
        
        # return self.dp[len(s1)][len(s2)]

        # Solution 3
        self.dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

        i = 1
        while i <= len(s1):
            j = 1
            while j <= len(s2):
                if s1[i-1] == s2[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1] + ord(s1[i-1])
                else:
                    self.dp[i][j] = max(self.dp[i][j-1], self.dp[i-1][j])
                j += 1
            i += 1
        
        sums1 = sum([ord(i) for i in s1])
        sums2 = sum([ord(i) for i in s2])
        return sums1 + sums2 - 2*self.dp[len(s1)][len(s2)]

print(Solution().minimumDeleteSum("sea",
"eat"))