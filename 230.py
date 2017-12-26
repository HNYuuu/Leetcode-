# 给一个BST, 计算第k小的值. 计算根节点的左子树
# 的节点个数, 和k做比较, 根据情况将根节点转换到
# 左孩子或右孩子上, 记得更改k的值

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def traverse(root):
            if root == None:
                return 0
            else:
                return 1+traverse(root.left)+traverse(root.right)
        
        while True:
            leftsum = traverse(root.left)
            if leftsum+1 == k:
                return root.val
            elif leftsum < k:
                root = root.right
                k = k - leftsum - 1
            else:
                root = root.left

a = TreeNode(1)
b = TreeNode(2)
a.right = b
print(Solution().kthSmallest(a,2))