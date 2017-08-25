# average of levels in binary tree
# practice for BFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = []
        q.append(root)
        open = []
        temp_result = 0
        result = []
        while True:
            length = len(q)
            if length == 0:
                break
            i = 0
            while i < length:
                # 这有一个坑，如果不是用open来判断左右子树而是q来判断是否存在的话，就会出现数组越界的bug
                open.append(q.pop(0))
                if open[i].left != None:
                    q.append(open[i].left)
                if open[i].right != None:
                    q.append(open[i].right)
                i += 1
            for i in open:
                temp_result += i.val
            result.append(float(temp_result)/len(open))
            del open[:]
            temp_result = 0
        return result     
