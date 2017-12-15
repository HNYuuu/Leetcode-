class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.tempSet = set()

        def t2s(root):
            if root.left != None:
                t2s(root.left)
            self.tempSet.add(root.val)
            if root.right != None:
                t2s(root.right)

        t2s(root)
        for i in self.tempSet:
            if k-i != i and k-i in self.tempSet:
                return True
        return False