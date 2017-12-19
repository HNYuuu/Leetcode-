# 将链表分组，任意两组之间的数量差不大于一。用当前链表
# 长度除以需要的分组数，向上取整，就是当前需要的节点数
# 量，随后长度减去刚才添加的，分组数减一，继续循环。最
# 后添加几个 None 即可

import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        head = root
        length = 0
        while head != None:
            length += 1
            head = head.next

        result = []
        head = root
        nextHead = root
        while length != 0 and k != 0:
            tempLength = math.ceil(length/k)
            i = 0
            while i < tempLength-1:
                nextHead = nextHead.next
                i += 1
            temp = nextHead.next
            nextHead.next = None
            result.append(head)
            head = temp
            nextHead = temp
            length -= tempLength
            k -= 1
        
        j = 0
        while j < k:
            result.append(None)
            j += 1

        return result

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
print(Solution().splitListToParts(a, 3))