# 给一个数组，通过数组构造一个最大二叉树。其规则是以当前数组的最
# 大值作为根，其左子树是该数左侧构成的最大二叉树，右子树同理。那
# 么用一个递归的结构，分别计算左右子树，边界情况：数组只有一个元
# 素那么其一定是叶节点。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def construct(nums):
            maximum = max(nums)
            position = nums.index(maximum)
            if position == 0:
                lSub = None
            else:
                lSub = construct(nums[:position])
            if position == len(nums)-1:
                rSub = None
            else:
                rSub = construct(nums[position+1:])
            root = TreeNode(maximum)
            root.left = lSub
            root.right = rSub
            return root

        return construct(nums)