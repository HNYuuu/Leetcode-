# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempHeadA = headA
        tempHeadB = headB
        countA = 0
        countB = 0
        if headA == None or headB == None:
            return None
        while tempHeadA != None:
            tempHeadA = tempHeadA.next
            countA += 1
        while tempHeadB != None:
            tempHeadB = tempHeadB.next
            countB += 1
        difference = countB-countA
        tempHeadA = headA
        tempHeadB = headB
        if difference > 0:
            for i in range(0, difference):
                tempHeadB = tempHeadB.next
        else:
            for i in range(0, -difference):
                tempHeadA = tempHeadA.next
        while tempHeadA != None:
            if tempHeadA == tempHeadB:
                return tempHeadA
            tempHeadA = tempHeadA.next
            tempHeadB = tempHeadB.next
        return None
    
