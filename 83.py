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
        temphead = head
        temp = set()
        if head:
            temp.add(head.val)
        else:
            return None
        while head.next != None:
            if head.next.val not in temp:
                temp.add(head.next.val)
                head = head.next
            else:
                head.next = head.next.next
        return temphead

a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c
print(Solution().deleteDuplicates(a))