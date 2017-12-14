# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None

        while head != None:
            if head.val == val:
                head = head.next

        if head == None:
            return None
        tempHead = head
        temp = head.next
        while temp != None:
            if temp.val == val:
                head.next = temp.next
            else:
                head = temp
            temp = temp.next
        
        return tempHead



