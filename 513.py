# 找到一个树的最下层的最左边的值。使用BFS算法，每一层的
# 节点值作为一个list扔到一个list中，从根向下遍历，直到
# 最底层。返回list的最后一个的第一个值即可

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        nodeValues = []
        queue.append(root)
        nodeCount = 1
        values = []
        while queue:
            tempNodeCount = nodeCount
            nodeCount = 0
            i = 0
            while i < tempNodeCount:
                tempNode = queue.pop(0)
                values.append(tempNode.val)
                if tempNode.left != None:
                    queue.append(tempNode.left)
                    nodeCount += 1
                if tempNode.right != None:
                    queue.append(tempNode.right)
                    nodeCount += 1
                i += 1
            nodeValues.append(values.copy())
            values.clear()
        return nodeValues[-1][0]

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
print(Solution().findBottomLeftValue(a))