# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use extra space
        # hash_table = set()
        # while head != None:
        #     if head in hash_table:
        #         return head
        #     hash_table.add(head)
        #     head = head.next
        # return None

        # without using extra space
        one = head
        two = head
        meet = None
        while one != None and two != None and two.next != None:
            one = one.next
            two = two.next.next
            if one == two:
                meet = one
                break

        if one == None or two == None or two.next == None:
            return None

        one = head
        while one != meet:
            one = one.next
            meet = meet.next
        return one

a = ListNode(1)
a.next = a
node = Solution().detectCycle(a)
print(node.val)