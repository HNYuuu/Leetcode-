# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leftHeight(node):
            h = 0
            while node:
                node = node.left
                h += 1
            return h

        def rightHeight(node):
            h = 0
            while node:
                node = node.right
                h += 1
            return h

        def traverse(node):
            if not node:
                return 0
            lh = leftHeight(node)
            rh = rightHeight(node)
            if lh == rh:
                return (1<<lh) - 1
            else:
                return traverse(node.left) + traverse(node.right) + 1

        return traverse(root)

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
c.left = f
print(Solution().countNodes(a))