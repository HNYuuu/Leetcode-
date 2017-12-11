# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        q = []
        temp = []
        q.append(s)
        while q:
            tempNode = q.pop(0)
            if tempNode.val == t.val:
                temp.append(tempNode)
            if tempNode.left != None:
                q.append(tempNode.left)
            if tempNode.right != None:
                q.append(tempNode.right)
        result = []
        for tempNode in temp:
            result.append(self.equal(tempNode, t))
        if True in result:
            return True
        else:
            return False
    
    def equal(self, s, t):
        if s.left != None and t.left != None and s.val == t.val:
            lResult = self.equal(s.left, t.left)
        elif s.left == None and t.left == None and s.val == t.val:
            lResult = True
        else: 
            lResult = False

        if s.right != None and t.right != None and s.val == t.val:
            rResult = self.equal(s.right, t.right)
        elif s.right == None and t.right == None and s.val == t.val: 
            rResult = True
        else: 
            rResult = False

        return lResult and rResult

a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)

f = TreeNode(4)
g = TreeNode(1)
h = TreeNode(2)

a.left = b
a.right = c
b.left = d
b.right = e

f.left = g
f.right = h

print(Solution().isSubtree(a, f))