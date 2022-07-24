class MyQueue(object):

    def __init__(self):
        self.stack_a = []
        self.stack_b = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_a.append(x)
        
    def shift(self):
        num = len(self.stack_a)
        for i in range(num):
            self.stack_b.append(self.stack_a.pop(0))
        
    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack_b):
            return self.stack_b.pop(0)
        else:
            self.shift()
            return self.stack_b.pop(0)
            

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack_b):
            return self.stack_b[0]
        else:
            self.shift()
            return self.stack_b[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_a)==0 and len(self.stack_b)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()