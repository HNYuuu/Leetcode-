# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isSame(root.left, root.right)
        
    def isSame(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            if node1.val == node2.val:
                return self.isSame(node1.left, node2.right) and self.isSame(node1.right, node2.left)
            else:
                return False