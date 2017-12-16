# 给一个有效的海图，数上面船只的数量。本来这种迷宫类题目是
# 想用DFS遍历的，每找到一个船点，就DFS其周围，将这只船的
# 所有点的坐标扔到已访问数组中。但是题目说这道题有一个one-pass
# 的解法，并且空间复杂度是O(1)，于是查了一下别人的思路。
# 发现只需要数船头即可，因此不妨假设所有的船的方向要么是朝
# 正北，要么是朝正西，于是一个双层遍历，判断好情况即可。

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        vertical = len(board)
        horizontal = len(board[0])
        shipCount = 0
        i, j = 0, 0
        while i < vertical:
            j = 0
            while j < horizontal:
                if i == 0 and j == 0 and board[i][j] == 'X':
                    shipCount += 1
                elif i == 0 and j > 0 and board[i][j] == 'X' and board[i][j-1] == '.':
                    shipCount += 1
                elif i > 0 and j == 0 and board[i][j] == 'X' and board[i-1][j] == '.':
                    shipCount += 1
                elif i > 0 and j > 0 and board[i][j] == 'X' and board[i-1][j] == '.' and board[i][j-1] == '.':
                    shipCount += 1
                j += 1
            i += 1
        return shipCount

print(Solution().countBattleships([[".","."],["X","X"]]))
