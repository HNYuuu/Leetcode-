# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        depthNum = 1
        turn = 0
        queue = []
        queue.append(root)
        temp = []
        array = []
        while queue:
            while turn < depthNum:
                temp.append(queue.pop(0))
                turn += 1
            depthNum = 0
            for tempNode in temp:
                if tempNode.left != None:
                    queue.append(tempNode.left)
                    depthNum += 1
                if tempNode.right != None:
                    queue.append(tempNode.right)
                    depthNum += 1
            turn = 0
            array.append([x.val for x in temp])
            temp.clear()
        return array

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e

print(Solution().levelOrderBottom(a))