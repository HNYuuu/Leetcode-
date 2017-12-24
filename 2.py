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
        p1 = l1
        p2 = l2
        cur = None
        carry = False
        head = None

        while p1 != None and p2 != None:
            if not carry and p1.val+p2.val > 9:
                carry = True
                tempNode = ListNode(p1.val+p2.val-10)
            elif carry and p1.val+p2.val >= 9:
                tempNode = ListNode(p1.val+p2.val+1-10)
            elif not carry and p1.val+p2.val <= 9:
                tempNode = ListNode(p1.val+p2.val)
            elif carry and p1.val+p2.val < 9:
                carry = False
                tempNode = ListNode(p1.val+p2.val+1)
            if cur == None:
                head = tempNode
            else:
                cur.next = tempNode
            cur = tempNode
            p1 = p1.next
            p2 = p2.next

        if p1 == None and p2 == None and not carry:
            pass
        elif p1 == None and p2 == None and carry:
            cur.next = ListNode(1)
        elif p1 == None and not carry:
            cur.next = p2
        elif p1 == None and carry:
            cur.next = p2
            if p2.val < 9:
                p2.val += 1
            else:
                while p2.next != None and p2.val == 9:
                    p2.val = p2.val+1-10
                    p2 = p2.next
                if p2.next == None and p2.val == 9:
                    p2.val = 0
                    p2.next = ListNode(1)
                elif p2.val != 9:
                    p2.val += 1
        elif p2 == None and not carry:
            cur.next = p1
        elif p2 == None and carry:
            cur.next = p1
            if p1.val < 9:
                p1.val += 1
            else:
                while p1.next != None and p1.val == 9:
                    p1.val = p1.val+1-10
                    p1 = p1.next
                if p1.next == None and p1.val == 9:
                    p1.val = 0
                    p1.next = ListNode(1)
                elif p1.val != 9:
                    p1.val += 1

        return head

a = ListNode(1)
b = ListNode(9)
c = ListNode(9)

b.next = c
print(Solution().addTwoNumbers(a, b))