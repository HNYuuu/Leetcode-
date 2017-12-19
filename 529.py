# 实现一个扫雷算法。没什么难度，DFS 遍历，
# 判断边界情况，注意相邻节点的坐标值的边界
# 条件

class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        # Judge if there is a mine nearby
        def mineAdjecent(node):
            i = node[0]
            j = node[1]
            adjecent = [(i-1, j), (i-1, j+1), (i-1, j-1), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j), (i+1, j-1)]
            for temp in adjecent:
                if temp in mines:
                    return True
            return False

        # Show the number of mines near a node
        def showNumber(node):
            i = node[0]
            j = node[1]
            count = 0
            if i+1 < vertical and board[i+1][j] == 'M':
                count += 1
            if j+1 < horizontal and board[i][j+1] == 'M':
                count += 1
            if i+1 < vertical and j+1 < horizontal and board[i+1][j+1] == 'M':
                count += 1
            if i > 0:
                if board[i-1][j] == 'M':
                    count += 1
                if j+1 < horizontal and board[i-1][j+1] == 'M':
                    count += 1
            if j > 0:
                if board[i][j-1] == 'M':
                    count += 1
                if i+1 < vertical and board[i+1][j-1] == 'M':
                    count += 1
            if i > 0 and j > 0:
                if board[i-1][j-1] == 'M':
                    count += 1
            board[i][j] = str(count)

        # Push adjecent nodes which are not in closeSet to stack
        def pushAdjecent(node, stack, close):
            i = node[0]
            j = node[1]
            if i+1 < vertical and (i+1, j) not in close:
                stack.append([i+1, j])
            if j+1 < horizontal and (i, j+1) not in close:
                stack.append([i, j+1])
            if i+1 < vertical and j+1 < horizontal and (i+1, j+1) not in close:
                stack.append([i+1, j+1])
            if i > 0:
                if (i-1, j) not in close:
                    stack.append([i-1, j])
                if j+1 < horizontal and (i-1, j+1) not in close:
                    stack.append([i-1, j+1])
            if j > 0:
                if (i, j-1) not in close:
                    stack.append([i, j-1])
                if i+1 < vertical and (i+1, j-1) not in close:
                    stack.append([i+1, j-1])
            if i > 0 and j > 0:
                if (i-1, j-1) not in close:
                    stack.append([i-1, j-1])

        vertical = len(board)
        horizontal = len(board[0])
        closeSet = set()
        stack = []
        mines = set()
        for i in range(0, vertical):
            for j in range(0, horizontal):
                if board[i][j] == 'M':
                    mines.add((i, j))
        
        # Click the mine
        if (click[0], click[1]) in mines:
            board[click[0]][click[1]] = 'X'
            return board
        # DFS
        else:
            stack.append(click)
            while stack:
                tempNode = stack.pop()
                closeSet.add((tempNode[0], tempNode[1]))
                if mineAdjecent(tempNode):
                    showNumber(tempNode)
                else:
                    board[tempNode[0]][tempNode[1]] = 'B'
                    pushAdjecent(tempNode, stack, closeSet)
            return board

print(Solution().updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
,[3,0]))

