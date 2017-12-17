# 返回一个二叉树的每一层的最大值。和昨天的一道题很
# 像，用BFS搜索每一层，把每一层的最大值添加到返回
# 数组即可。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        q = []
        q.append(root)
        nodeForLayer = 1
        layerValue = []
        result = []
        while q:
            i = 0
            tempNodeForLayer = nodeForLayer
            nodeForLayer = 0
            while i < tempNodeForLayer:
                tempNode = q.pop(0)
                layerValue.append(tempNode.val)
                if tempNode.left != None:
                    q.append(tempNode.left)
                    nodeForLayer += 1
                if tempNode.right != None:
                    q.append(tempNode.right)
                    nodeForLayer += 1
                i += 1
            result.append(layerValue.copy())
            layerValue.clear()
        returnValue = []
        for layer in result:
            returnValue.append(max(layer))
        return returnValue

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(Solution().largestValues(a))
