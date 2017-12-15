# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.tilt = 0

        def calc(root):
            if root.left != None:
                lsum = calc(root.left)
            else:
                lsum = 0
            if root.right != None:
                rsum = calc(root.right)
            else:
                rsum = 0
            self.tilt += abs(lsum-rsum)
            return lsum+rsum+root.val

        calc(root)
        return self.tilt

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.left = b
a.right = c
b.left = d
print(Solution().findTilt(a))