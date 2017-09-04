# second minimum node in a binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        self.recursive(root, result)
        result = set(result)
        if len(result) == 1:
            return -1
        else:
            result = list(result)
            result.sort()
            return result[1]
        
    def recursive(self, root, result):
        result.append(root.val)
        if root.left:
            self.recursive(root.left, result)
            self.recursive(root.right, result)
        else:
            return
