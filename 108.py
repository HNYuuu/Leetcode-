# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def A2B(l, m, r, nums):
            root = TreeNode(nums[m])
            root.left = A2B(l, (m-1-l)//2+l, m-1, nums) if l <= m-1 else None
            root.right = A2B(m+1, (r-m-1)//2+m+1, r, nums) if m+1 <= r else None
            return root
        
        if nums == []:
            return None
        left = 0
        right = len(nums)-1
        mid = (right-left)//2
        root = A2B(left, mid, right, nums)
        return root

print(Solution().sortedArrayToBST([0,1,2,3,4,5]))