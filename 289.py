class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def calc_cells(i, j):
            count = 0
            if i > 0:
                if j > 0 and (board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == 3):
                    count += 1
                if (board[i - 1][j] == 1 or board[i - 1][j] == 3):
                    count += 1
                if j < len(board[0]) - 1 and (board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == 3):
                    count += 1
            if j > 0 and (board[i][j - 1] == 1 or board[i][j - 1] == 3):
                count += 1
            if j < len(board[0]) - 1 and (board[i][j + 1] == 1 or board[i][j + 1] == 3):
                count += 1
            if i < len(board) - 1:
                if j > 0 and (board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == 3):
                    count += 1
                if (board[i + 1][j] == 1 or board[i + 1][j] == 3):
                    count += 1
                if j < len(board[0]) - 1 and (board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == 3):
                    count += 1
            return count

        for i in range(len(board)):
            for j in range(len(board[0])):
                count = calc_cells(i, j)
                if (count < 2 or count > 3) and board[i][j] == 1:
                    board[i][j] = 3
                elif count == 3 and board[i][j] == 0:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0