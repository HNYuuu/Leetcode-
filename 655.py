# 给一个二叉树，返回一个二维数组，这个数组反映了树的构形。思路是先 DFS 
# 树的最大深度，根据深度可以构造一个没有任何值但是符合长宽的二维数组，
# 然后再来一个先序遍历，要标明左界限、右界限和深度，这样可以根据这几个
# 参数填入构造好的二维数组中

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.maxDepth = 0

        def getDepth(root, depth):
            if root.left != None:
                getDepth(root.left, depth+1)
            if root.right != None:
                getDepth(root.right, depth+1)
            if root.left == None and root.right == None:
                if depth > self.maxDepth:
                    self.maxDepth = depth
                return
        
        getDepth(root, 0)

        result = [['' for i in range(2**(self.maxDepth+1)-1)] for j in range(self.maxDepth+1)]

        l = 0
        r = len(result[0])-1
        def fillBlank(l, r, root, depth):
            m = (r-l)//2+l
            result[depth][m] = str(root.val)
            if root.left != None:
                fillBlank(l, m, root.left, depth+1)
            if root.right != None:
                fillBlank(m+1, r, root.right, depth+1)
            return

        fillBlank(l, r, root, 0)
        
        return result

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
d.right = e
print(Solution().printTree(a))
