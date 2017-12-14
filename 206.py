# reverse linked list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        self.tempHead = None

        def reverse(head):
            if head.next.next != None:
                reverse(head.next)
            else:
                self.tempHead = head.next
            head.next.next = head
        
        reverse(head)
        head.next = None
        return self.tempHead

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
s = Solution()
print(s.reverseList(a).val)

