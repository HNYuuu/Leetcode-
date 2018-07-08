class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i for i in range(1, n+1)]

        store = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n+1):
            store[i][i] = 0
            if i+1<n+1:
                store[i][i+1] = 0
            if i+2<n+1:
                store[i][i+2] = nums[i]
            if i+3<n+1:
                store[i][i+3] = nums[i+1]


        def dp(i, j):
            if store[i][j] != -1:
                # print('hit')
                return store[i][j]
            else:
                temp = set()
                # for k in range(i+(j-1)//2-1, j):
                for k in range(i, j):
                    lr = dp(i,k)
                    rr = dp(k+1,j)
                    temp.add(nums[k]+(lr if lr>rr else rr))
                store[i][j] = min(temp)
                return store[i][j]

        return dp(0, n)

print(Solution().getMoneyAmount(200))