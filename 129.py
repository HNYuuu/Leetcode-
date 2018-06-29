# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = []

        def traverse(node, data):
            if not node.left and not node.right:
                data.append(str(node.val))
                result.append(''.join(data))
                data.pop()
            else:
                data.append(str(node.val))
                if node.left:
                    traverse(node.left, data)
                if node.right:
                    traverse(node.right, data)
                data.pop()

        traverse(root, [])
        result = [int(x) for x in result]
        return sum(result)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
print(Solution().sumNumbers(a))