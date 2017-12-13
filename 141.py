# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        run1 = head
        run2 = head
        while run1.next != None and run2.next.next != None:
            run1 = run1.next
            run2 = run2.next.next
            if run1 == run2:
                return True
        return False