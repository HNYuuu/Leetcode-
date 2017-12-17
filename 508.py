# 返回一个树出现频率最高的节点值（当前节点与其子节点值之和）

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        # key = node.val
        # value = how many times appeare
        self.count = {}

        def calc(root):
            if root.left != None:
                ls = calc(root.left)
            else:
                ls = 0
            if root.right != None:
                rs = calc(root.right)
            else:
                rs = 0
            result = root.val + ls + rs
            if result not in self.count.keys():
                self.count[result] = 1
            else:
                self.count[result] += 1
            return result
            
        calc(root)
        # find the maximum
        maximum = max(self.count.values())
        # because there may be a tie, use list to append node value
        result = []
        for node in self.count:
            if self.count[node] == maximum:
                result.append(node)
        
        return result
