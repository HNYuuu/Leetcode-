# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        dummy = ListNode(0)
        cur = dummy
        dummy.next = head
        nxt = head
        flag = False

        while nxt.next != None:
            if nxt.val == nxt.next.val:
                nxt = nxt.next
                cur.next = nxt
                flag = True
            elif flag:
                nxt = nxt.next
                cur.next = nxt
                flag = False
            else:
                cur = nxt
                nxt = nxt.next
        if flag:
            cur.next = nxt.next
        return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
g = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
Solution().deleteDuplicates(a)