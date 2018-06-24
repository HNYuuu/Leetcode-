# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None

        less, more = [], []
        tmp = head
        while tmp != None:
            if tmp.val < x:
                less.append(tmp.val)
            else:
                more.append(tmp.val)
            tmp = tmp.next

        tmp_less = None
        if len(less) > 0:
            for i in range(len(less)-1, -1, -1):
                cur = ListNode(less[i])
                cur.next = tmp_less
                tmp_less = cur
        else:
            pass

        tmp = None
        if len(more) > 0:
            for i in range(len(more)-1, -1, -1):
                cur = ListNode(more[i])
                cur.next = tmp
                tmp = cur
        else:
            pass

        if len(less) == 0:
            return tmp
        elif len(more) == 0:
            return tmp_less
        else:
            dummy = ListNode(0)
            dummy.next = tmp_less
            tmp_return = tmp_less
            while tmp_return.next != None:
                tmp_return = tmp_return.next
            tmp_return.next = tmp
            return dummy.next