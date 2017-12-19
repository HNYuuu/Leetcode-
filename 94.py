# 中序遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        result = []
        def traversal(root):
            if root.left != None:
                traversal(root.left)
            result.append(root.val)
            if root.right != None:
                traversal(root.right)
        
        traversal(root)
        return result

