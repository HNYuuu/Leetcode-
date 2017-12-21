# 构造一个类包括一个函数可以随机返回一个链表中的节点
# 值. 因为长度不知, 所以使用蓄水池采样法, 这样可以
# 保证在边读边采样的情况下可以最公平的找到 k 个元素

import random

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.temp = head
        self.reservoir = [head.val]

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        self.reservoir = [self.temp.val]
        temp = self.temp.next
        i = 2
        while temp != None:
            probability = random.randrange(1, i+1)
            if probability == 1:
                self.reservoir = [temp.val]
            temp = temp.next
            i += 1
        return self.reservoir[0]



# Init a singly linked list [1,2,3].
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution(head)

# getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())
print(solution.getRandom())