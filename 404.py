# sum of left leaves

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        array = []
        flag = True
        self.leftLeavesToArray(root, array, flag)
        # return array
        value = 0
        for i in array:
            value += i.val
        return value
        
    def leftLeavesToArray(self, root, a, flag):
        if root.left != None:
            flag = False
            self.leftLeavesToArray(root.left, a, flag)
            flag = True
        if root.right != None:
            flag = True
            self.leftLeavesToArray(root.right, a, flag)
        if flag:
            return
        else:
            a.append(root)

a = TreeNode(3)
b = TreeNode(9)
# c = TreeNode(20)
# d = TreeNode(15)
# e = TreeNode(7)
a.left = b
# a.right = c
# c.left = d
# c.right = e
print(Solution().sumOfLeftLeaves(a))
print(b)
# print(d)
# print(e)