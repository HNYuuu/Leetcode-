class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        i = 0
        temp = []
        while i < len(self.stack)-1:
            temp.append(self.stack.pop(0))
        tempVal = self.stack.pop(0)
        self.stack = temp.copy()
        return tempVal
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return True if len(self.stack) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
obj.push(6)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2, param_3, param_4)