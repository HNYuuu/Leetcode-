# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        doing = []

        def traverse(node):
            doing.append(node)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)

        for i in range(len(doing) - 1):
            doing[i].right = doing[i + 1]
            doing[i].left = None
        doing[-1].right = None