# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        final_result = []

        def backtrack(node, data):
            if node.left == None and node.right == None:
                data.append(node.val)
                result.append(data.copy())
                data.pop()
            else:
                data.append(node.val)
                if node.left != None:
                    backtrack(node.left, data)
                if node.right != None:
                    backtrack(node.right, data)
                data.pop()

        backtrack(root, [])
        for i in result:
            if sum(i) == target:
                final_result.append(i)

        return final_result