# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None

        dummy = RandomListNode(0)
        new_head = RandomListNode(head.label)
        dummy.next = new_head
        temp_head = head
        # map old node to new node
        node_map = {}
        node_map[head] = new_head

        while head != None:
            head = head.next
            if head != None:
                new_head.next = RandomListNode(head.label)
            else:
                new_head.next = None
            new_head = new_head.next
            node_map[head] = new_head

        head = temp_head
        new_head = dummy.next
        while head != None:
            if head.random == None:
                new_head.random = None
            else:
                new_head.random = node_map[head.random]

            new_head = new_head.next
            head = head.next

        return dummy.next

a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
a.next = b
b.next = c
a.random = c
b.random = None
c.random = b

node = Solution().copyRandomList(a)
print(node.label)
