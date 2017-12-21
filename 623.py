# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            temp = TreeNode(v)
            temp.left = root
            return temp

        def traverse(root, depth):
            if depth + 1 == d:
                lchild = root.left
                rchild = root.right
                templ = TreeNode(v)
                tempr = TreeNode(v)
                root.left = templ
                templ.left = lchild
                root.right = tempr
                tempr.right = rchild
                return
            if root.left != None:
                traverse(root.left, depth+1)
            if root.right != None:
                traverse(root.right, depth+1)
        
        traverse(root, 1)
        return root