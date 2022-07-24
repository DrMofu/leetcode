class MyStack(object):

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        num = len(self.queue)
        self.queue.append(x)
        for i in range(num):
            self.queue.append(self.queue.pop(0))
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()