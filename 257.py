# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        result = self.t2a(root)
        return [x[2:] for x in result]
        
    def t2a(self, root):
        lr, rr, result = [], [], []
        if root.left != None:
            lr = self.t2a(root.left)
        if root.right != None:
            rr = self.t2a(root.right)
        if len(lr) == 0 and len(rr) == 0:
            return ['->'+str(root.val)]
        else:
            lr.extend(rr)
            for temp in lr:
                result.append('->'+str(root.val)+temp)
            return result

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
print(Solution().binaryTreePaths(e))