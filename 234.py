# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        elif head.next == None:
            return True

        slow = head
        fast = head
        count = 0

        while fast.next != None:
            slow = slow.next
            fast = fast.next.next
            count += 1
            if fast == None:
                break
        
        self.tempHead = None

        def reverse(head):
            t1 = head.next
            t2 = t1.next
            head.next = None
            while t2 != None:
                t1.next = head
                head = t1
                t1 = t2
                t2 = t2.next
            t1.next = head
            self.tempHead = t1
        
        if slow.next == None:
            self.tempHead = slow
            slow.next = None
        else:
            reverse(slow)

        if fast == None:
            i = 0
            while i < count:
                if self.tempHead.val != head.val:
                    return False
                self.tempHead = self.tempHead.next
                head = head.next
                i += 1
            return True
        else:
            i = 0
            while i < count+1:
                if self.tempHead.val != head.val:
                    return False
                self.tempHead = self.tempHead.next
                head = head.next
                i += 1
            return True

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e
print(Solution().isPalindrome(a))
