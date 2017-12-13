# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        def getDepth(root):
            if root.left == None and root.right == None:
                return 0
            elif root.left == None:
                return getDepth(root.right)+1
            elif root.right == None:
                return getDepth(root.left)+1
            else:
                return min(getDepth(root.left), getDepth(root.right))+1

        return getDepth(root)

    
