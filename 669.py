# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        if root.left != None:
            root.left = self.trimBST(root.left, L, R)
        if root.right != None:
            root.right = self.trimBST(root.right, L, R)

        if root.val < L:
            return root.right
        if root.val > R:
            return root.left
        return root

a = TreeNode(1)
b = TreeNode(0)
c = TreeNode(2)
a.left = b
a.right = c
print(Solution().trimBST(a, 1, 2))