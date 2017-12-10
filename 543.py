# Definition for a binary tree node.
class TreeNode:
    def __init__(self):
        self.val = 1
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def depth(p):
            if p == None:
                return 0
            leftDepth, rightDepth = depth(p.left), depth(p.right)
            self.ans = max(self.ans, leftDepth+rightDepth)
            return 1 + max(leftDepth, rightDepth)
            
        depth(root)
        return self.ans

a = TreeNode()
b = TreeNode()
c = TreeNode()
d = TreeNode()
e = TreeNode()
f = TreeNode()
g = TreeNode()
h = TreeNode()
i = TreeNode()
j = TreeNode()
k = TreeNode()
l = TreeNode()
m = TreeNode()
n = TreeNode()
o = TreeNode()
p = TreeNode()
q = TreeNode()
r = TreeNode()

a.left = b
a.right = c
c.left = d
c.right = e
e.left = f
d.left = g
d.right = h
g.left = i
i.left = j
i.right = k
j.right = l
k.left = m
h.left = n
n.left = o
h.right = p
p.left = q
q.left = r

print(Solution().diameterOfBinaryTree(i))