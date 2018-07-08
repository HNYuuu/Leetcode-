# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None

        needed = [root]
        temp = set()
        while len(needed) > 0:
            temp = set(needed.copy())
            length = len(needed)
            for _ in range(length):
                node = needed.pop(0)
                if node.left:
                    needed.append(node.left)
                if node.right:
                    needed.append(node.right)

        count = [0]
        def traverse(node):
            if not node:
                return []
            else:
                lr = traverse(node.left)
                rr = traverse(node.right)
                if isinstance(lr, TreeNode):
                    return lr
                if isinstance(rr, TreeNode):
                    return rr
                this_layer = [node]+lr+rr
                if temp.issubset(this_layer):
                    return node
                else:
                    return this_layer

        return traverse(root)

# a = TreeNode(1)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# f = TreeNode(6)
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# print(Solution().subtreeWithAllDeepest(a).val)