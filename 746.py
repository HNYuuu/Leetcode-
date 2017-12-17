class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        self.cache = [-1] * (len(cost))
        self.cache[0] = cost[0]
        self.cache[1] = cost[1]
        self.cache[-1] = 0

        def calc(stair):
            if stair == 0:
                return self.cache[0]
            elif stair == 1:
                return self.cache[1]
            else:
                if self.cache[stair-1] != -1:
                    temp1 = self.cache[stair-1]
                else:
                    temp1 = calc(stair-1)
                if self.cache[stair-2] != -1:
                    temp2 = self.cache[stair-2]
                else:
                    temp2 = calc(stair-2)
                self.cache[stair] = min(cost[stair]+temp1, cost[stair]+temp2)
                return self.cache[stair]

        return calc(len(cost)-1)

print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))