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
        result = []
        temp = head
        result.append(head.val)
        while head.next != None:
            head = head.next
            result.append(head.val)
        head = temp
        result.reverse()
        for i in result:
            head.val = i
            head = head.next
        head = temp
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
s = Solution()
s.reverseList(a)
print(a.val)

