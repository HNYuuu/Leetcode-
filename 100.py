# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        arrayp = []
        arrayq = []
        if p == None and q == None:
            return True
        elif p != None and q != None:
            self.treeToArray(p, arrayp)
            self.treeToArray(q, arrayq)
        else:
            return False
        if len(arrayp) != len(arrayq):
            return False
        else:
            i, j = 0, 0
            while i < len(arrayp):
                if arrayp[i] != arrayq[j]:
                    return False
                i += 1
                j += 1
            return True

    def treeToArray(self, root, a):
        if root.left != None:
            self.treeToArray(root.left, a)
        a.append(-1)
        a.append(root.val)
        if root.right != None:
            self.treeToArray(root.right, a)
        a.append(-1)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(1)
e = TreeNode(2)
f = TreeNode(3)
a.left = b
a.right = c
d.left = e
d.right = f
print(Solution().isSameTree(a,d))