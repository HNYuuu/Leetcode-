# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        elif l1 == None or l2 == None:
            return l1 if l2 == None else l2
        head = ListNode(0)
        mark = head
        while True:
            if l1.val == l2.val:
                nodeA = l1
                nodeB = l2
                l1 = l1.next
                l2 = l2.next
                head.next = nodeA
                nodeA.next = nodeB
                head = nodeB
            elif l1.val < l2.val:
                nodeA = l1
                l1 = l1.next
                head.next = nodeA
                head = nodeA
            else:
                nodeA = l2
                l2 = l2.next
                head.next = nodeA
                head = nodeA
            if l1 == None and l2 == None:
                return mark.next
            elif l1 != None and l2 != None:
                continue
            else:
                head.next = l1 if l2 == None else l2
                return mark.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
a.next = b
b.next = c
d.next = e
e.next = f
print(Solution().mergeTwoLists(a,d))