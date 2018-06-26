# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        value = []
        while head != None:
            value.append(head.val)
            head = head.next

        def construct(v):
            if len(v) == 0:
                return None
            root = TreeNode(v[len(v)//2])
            if len(v) == 1:
                return root
            root.left = construct(v[:len(v)//2])
            root.right = construct(v[len(v)//2+1:])
            return root

        return construct(value)