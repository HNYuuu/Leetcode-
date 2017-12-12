# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.result = {}

        def traverse(root):
            if root.left != None:
                traverse(root.left)
            if root.val not in self.result.keys():
                self.result[root.val] = 1
            else:
                self.result[root.val] += 1
            if root.right != None:
                traverse(root.right)

        traverse(root)
        maximum = max(self.result.values())
        temp = []
        for i in self.result.keys():
            if self.result[i] == maximum:
                temp.append(i)
        return temp