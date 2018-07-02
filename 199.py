# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        need = []
        result = []

        need.append(root)
        result.append(root.val)
        while len(need)>0:
            length = len(need)
            for _ in range(length):
                node = need.pop(0)
                if node.left:
                    need.append(node.left)
                if node.right:
                    need.append(node.right)
            if len(need) > 0:
                result.append(need[-1].val)
        return result

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.right = e
c.right = d
print(Solution().rightSideView(a))