# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # return (next layer.val, this layer's val)
        def traverse(root):
            if root == None:
                return (0, 0)
            elif not root.left and not root.right:
                return (0, root.val)
            else:
                lr = traverse(root.left)
                rr = traverse(root.right)

                return (max(lr[0] + rr[0], lr[0] + rr[1], lr[1] + rr[0], lr[1] + rr[1]), root.val + lr[0] + rr[0])

        return max(traverse(root))


# a = TreeNode(3)
# b = TreeNode(2)
# c = TreeNode(3)
# d = TreeNode(3)
# e = TreeNode(1)
# a.left = b
# a.right = c
# b.right = d
# c.right = e
# print(Solution().rob(a))
