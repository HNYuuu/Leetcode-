# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def traverse(node):
            lr, rr = [], []
            if node.left:
                lr = traverse(node.left)
            if node.right:
                rr = traverse(node.right)
            if not node.left and not node.right:
                return [node.val]
            else:
                if isinstance(lr, TreeNode):
                    return lr
                elif isinstance(rr, TreeNode):
                    return rr
                else:
                    temp = lr + rr + [node.val]
                    if p.val in temp and q.val in temp:
                        return node
                    else:
                        return temp

        return traverse(root)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
print(Solution().lowestCommonAncestor(a, d, e).val)