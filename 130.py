class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == [[]]:
            return

        # get the O on the margin
        margin = set()
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                margin.add((0, j))
            if board[-1][j] == 'O':
                margin.add((len(board) - 1, j))
        for i in range(len(board)):
            if board[i][0] == 'O':
                margin.add((i, 0))
            if board[i][-1] == 'O':
                margin.add((i, len(board[0]) - 1))

        # get O adjacent to margin O
        need = margin
        visited = set()
        while len(need) > 0:
            i, j = need.pop()
            if (i, j) in visited:
                continue
            else:
                visited.add((i, j))
            if i > 0 and board[i - 1][j] == 'O' and (i - 1, j) not in visited:
                need.add((i - 1, j))
            if i < len(board) - 1 and board[i + 1][j] == 'O' and (i + 1, j) not in visited:
                need.add((i + 1, j))
            if j < len(board[0]) - 1 and board[i][j + 1] == 'O' and (i, j + 1) not in visited:
                need.add((i, j + 1))
            if j > 0 and board[i][j - 1] == 'O' and (i, j - 1) not in visited:
                need.add((i, j - 1))

        # traverse the whole board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'

print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
