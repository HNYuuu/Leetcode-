class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        y = len(grid[0])
        x = len(grid)
        queue = []
        result = 0
        maxArea = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    result = self.bfs(grid, x, y, queue)
                    if maxArea < result:
                        maxArea = result
        return maxArea

    
    def bfs(self, grid, x, y, q):
        result = 0
        while q:
            start = q.pop(0)
            i = start[0]
            j = start[1]
            if grid[i][j] == 1:
                grid[i][j] = 0
                result += 1
            else:
                continue
            if i > 0 and grid[i-1][j] == 1:
                q.append((i-1,j))
            if i < x-1 and grid[i+1][j] == 1:
                q.append((i+1,j))
            if j > 0 and grid[i][j-1] == 1:
                q.append((i,j-1))
            if j < y-1 and grid[i][j+1] == 1:
                q.append((i,j+1))
        return result

print(Solution().maxAreaOfIsland([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))