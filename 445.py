# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = ''
        val2 = ''
        head = l1
        while head != None:
            val1 += str(head.val)
            head = head.next
        head = l2
        while head != None:
            val2 += str(head.val)
            head = head.next
        
        result = str(int(val1)+int(val2))
        head = None
        cur = None
        for i in result:
            tempNode = ListNode(i)
            if cur == None:
                cur = tempNode
                head = tempNode
            else:
                cur.next = tempNode
                cur = cur.next

        return head
