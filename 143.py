# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return

        dummy_1, dummy_2 = ListNode(0), ListNode(0)
        dummy_1.next = head
        temp_head = head

        length = 0
        while head != None:
            head = head.next
            length += 1

        half = length//2
        head = temp_head
        for i in range(half):
            head = head.next
        dummy_2.next = head.next
        head.next = None

        cur, nxt = None, dummy_2.next
        tmp = nxt.next
        while True:
            nxt.next = cur
            cur = nxt
            nxt = tmp
            if tmp == None:
                break
            tmp = tmp.next
        dummy_2.next = cur

        temp_head_1, temp_head_2 = dummy_1.next, dummy_2.next
        tmp1, tmp2 = temp_head_1.next, temp_head_2.next
        while True:
            temp_head_1.next = temp_head_2
            temp_head_2.next = tmp1
            if tmp1 == None or tmp2 == None:
                break
            temp_head_1 = tmp1
            temp_head_2 = tmp2
            tmp1 = tmp1.next
            tmp2 = tmp2.next

        head = dummy_1.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
# d.next = e
node1 = Solution().reorderList(a)
print(node1)