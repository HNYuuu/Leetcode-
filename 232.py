class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = [0]*(len(self.queue)-1)
        i = 0
        length = len(self.queue)
        while i < length-1:
            temp.append(self.queue.pop())
            i += 1
        tempVal = self.queue.pop()
        i = 0
        while i < length-1:
            self.queue.append(temp.pop())
            i += 1
        return tempVal


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return True if len(self.queue) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
# obj.push(3)
param_2 = obj.pop()
# print(param_2)
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)