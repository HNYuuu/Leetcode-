class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for j in range(len(grid[0])):
            result[0][j] = sum(grid[0][:j+1])
        grid_dup = list(zip(*grid))
        for i in range(len(grid_dup[0])):
            result[i][0] = sum(grid_dup[0][:i+1])

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                result[i][j] = min(result[i-1][j], result[i][j-1]) + grid[i][j]

        return result[-1][-1]

print(Solution().minPathSum([
  [1],
]))