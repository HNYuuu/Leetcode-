# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        def link(l, r):
            l.next = r
            temp = []
            if l.left: temp.append(l.left)
            if l.right: temp.append(l.right)
            if r.left: temp.append(r.left)
            if r.right: temp.append(r.right)
            if len(temp) > 1:
                for i in range(len(temp)-1):
                    link(temp[i], temp[i+1])
        if root == None:
            return
        elif not root.left and not root.right:
            root.next = None
        elif not root.right:
            root.left.next = None
        elif not root.left:
            root.right.next = None
        else:
            link(root.left, root.right)

# a = TreeLinkNode(1)
# b = TreeLinkNode(2)
# c = TreeLinkNode(3)
# a.left = b
# a.right = c
# Solution().connect(a)