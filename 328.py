# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head.next == None:
            return head
        odd = head
        even = head.next
        evenhead = head.next
        while True:
            if even.next != None:
                odd.next = even.next
            else:
                odd.next = evenhead
                return head
            if odd.next.next != None:
                even.next = odd.next.next
            else:
                even.next = None
                odd.next.next = evenhead
                return head
            odd = odd.next
            even = even.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
print(Solution().oddEvenList(a))