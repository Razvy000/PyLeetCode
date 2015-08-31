'''
Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''


from collections import deque

class L225_Implement_Stack_using_Queues_Ezy:
    
    # initialize your data structure here.
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)

    # @return nothing
    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        

    # @return an integer
    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        toppy = self.q1.popleft()
        self.q2.append(toppy)
        self.q1, self.q2 = self.q2, self.q1
        return toppy

    # @return an boolean
    def empty(self):
        return len(self.q1) == 0
        
        