# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0 
        result = self.treeSum(root)
        return True if sum in result else False

    def treeSum(self, root):
        lsum, rsum, temp = [], [], []
        if root.left != None:
            lsum = self.treeSum(root.left)
        else:
            lsum = []
        if root.right != None:
            rsum = self.treeSum(root.right)
        else:
            rsum = []
        if len(lsum) == 0 and len(rsum) == 0:
            return [root.val]
        else:
            lsum.extend(rsum)
            for i in lsum:
                i += root.val
                temp.append(i)
            return temp

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(Solution().pathSum(a, 10))