# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        array = []
        valArray = []
        self.treeToList(root, array)
        # return array
        for i in array:
            valArray.append(i.val)
        for i in range(len(array)):
            array[i].val = sum(valArray[i:])
        return root


    def treeToList(self, root, a):
        if root.left != None:
            self.treeToList(root.left, a)
        a.append(root)
        if root.right != None:
            self.treeToList(root.right, a)

a = TreeNode(5)
b = TreeNode(2)
c = TreeNode(13)
a.left = b
a.right = c
print(Solution().convertBST(a))
print(a)

