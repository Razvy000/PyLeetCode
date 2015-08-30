'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
'''

class L155_Min_Stack_Ezy:
    
    # initialize your data structure here.
    def __init__(self):
        self.S1 = []
        self.S2 = [] # stack of minimums

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.S1.append(x)
        if not self.S2 or self.S2[-1] >= x:
            self.S2.append(x)

    # @return nothing
    def pop(self):
        x = self.S1.pop()
        if self.S2 and self.S2[-1] == x:
            self.S2.pop()
        

    # @return an integer
    def top(self):
        return self.S1[-1]
        

    # @return an integer
    def getMin(self):
        if self.S2:
            return self.S2[-1]
        return 0