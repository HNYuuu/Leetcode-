# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        l, r = head, head.next
        dummy = ListNode(0)
        dummy.next = r

        def traverse(l, r):
            if l == None:
                return None
            elif r == None:
                return l
            temp = r.next
            r.next = l
            if temp == None:
                l.next = traverse(None, None)
            else:
                l.next = traverse(temp, temp.next)
            return r

        return traverse(l, r)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
Solution().swapPairs(a)