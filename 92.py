class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        cur = new_head
        for _ in range(m-1):
            cur = cur.next
        new_tail = cur
        dummy = ListNode(0)
        dummy.next = cur.next
        new_dummy = dummy.next
        cur = dummy
        nxt = cur.next

        for _ in range(n-m+1):
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp

        new_tail.next = cur
        new_dummy.next = tmp
        return new_head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
Solution().reverseBetween(a, 2, 4)