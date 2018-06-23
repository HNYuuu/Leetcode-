class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        result = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
        flag = False
        for j in range(len(obstacleGrid[0])):
            if result[0][j] != 0 and not flag:
                result[0][j] = 1
            elif result[0][j] == 0:
                flag = True
            elif flag:
                result[0][j] = 0

        flag = False
        for i in range(len(obstacleGrid)):
            if result[i][0] != 0 and not flag:
                result[i][0] = 1
            elif result[i][0] == 0:
                flag = True
            elif flag:
                result[i][0] = 0

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if result[i][j] == 0:
                    continue
                elif result[i][j] == -1:
                    result[i][j] = result[i-1][j] + result[i][j-1]

        return result[-1][-1]

print(Solution().uniquePathsWithObstacles([
  [0,1,0],
]
))