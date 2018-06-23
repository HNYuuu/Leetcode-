# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        dummy = ListNode(0)
        tail = head
        length = 1
        while tail.next != None:
            tail = tail.next
            length += 1
        tail.next = head

        k %= length
        temp = head
        for _ in range(length-k-1):
            temp = temp.next
        dummy.next = temp.next
        temp.next = None
        return dummy.next
