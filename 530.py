# minimum absolute difference in BST

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        self.solution(root, result)
        min = float('inf')
        for i in range(len(result)-1):
            if result[i+1] - result[i] < min:
                min = result[i+1] - result[i]
        return min

    def solution(self, root, result):
        if root.left:
            self.solution(root.left, result)
        result.append(root.val)
        if root.right:
            self.solution(root.right, result)