# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True

        def depth(root):
            ld, rd = 0, 0
            if root.left != None:
                ld = depth(root.left)
            if root.right != None:
                rd = depth(root.right)
            if abs(ld-rd) > 1:
                self.flag = False
            return max(ld, rd)+1

        if root != None:
            depth(root)
            return self.flag
        else:
            return True