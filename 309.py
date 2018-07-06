class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # this is dp, but it is not good
        # store = [[-1 for _ in range(len(prices)+1)] for _ in range(len(prices))]
        #
        # for i in range(len(prices)):
        #     store[i][i] = 0
        #     store[i][i+1] = 0
        #
        # def dp(i, j):
        #     if i == j or i+1 == j:
        #         return 0
        #     elif store[i][j] != -1:
        #         # print('hit')
        #         return store[i][j]
        #     else:
        #         now_max = 0
        #         for k in range(i, j):
        #             if (dp(i, k)+dp(k+1, j)) > now_max:
        #                 now_max = (dp(i, k)+dp(k+1, j))
        #         if (prices[j-1]-prices[i]) > now_max:
        #             now_max = (prices[j-1]-prices[i])
        #         store[i][j] = now_max
        #         return store[i][j]
        #
        # return dp(0, len(prices))

        if len(prices) <= 1:
            return 0
        s0 = -prices[0]
        s1 = -2**32
        s2 = 0
        for i in range(1, len(prices)):
            pre0, pre1, pre2 = s0, s1, s2
            s0 = max(pre2-prices[i], pre0)
            s1 = pre0+prices[i]
            s2 = max(pre2, pre1)
        return max(s1, s2)

# print(Solution().maxProfit([1,2,3]))

# print(Solution().maxProfit([70,4,83,56,94,72,78,43,2,86,65,100,94,56,41,66,3,33,10,3,45,94,15,12,78,60,58,0,58,15,21,7,11,41,12,96,83,77,47,62,27,19,40,63,30,4,77,52,17,57,21,66,63,29,51,40,37,6,44,42,92,16,64,33,31,51,36,0,29,95,92,35,66,91,19,21,100,95,40,61,15,83,31,55,59,84,21,99,45,64,90,25,40,6,41,5,25,52,59,61,51,37,92,90,20,20,96,66,79,28,83,60,91,30,52,55,1,99,8,68,14,84,59,5,34,93,25,10,93,21,35,66,88,20,97,25,63,80,20,86,33,53,43,86,53,55,61,77,9,2,56,78,43,19,68,69,49,1,6,5,82,46,24,33,85,24,56,51,45,100,94,26,15,33,35,59,25,65,32,26,93,73,0,40,92,56,76,18,2,45,64,66,64,39,77,1,55,90,10,27,85,40,95,78,39,40,62,30,12,57,84,95,86,57,41,52,77,17,9,15,33,17,68,63,59,40,5,63,30,86,57,5,55,47,0,92,95,100,25,79,84,93,83,93,18,20,32,63,65,56,68]))