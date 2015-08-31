'''
Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.
'''


class L232_Implement_Queue_using_Stacks_Ezy:
    
    # initialize your data structure here.
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s1.append(x)
        

    # @return nothing
    def pop(self):
        self.fill(self.s1, self.s2)
        self.s2.pop()
        self.fill(self.s2, self.s1)

    def fill(self, a, b):
        while len(a):
            b.append(a.pop())
    
    # @return an integer
    def peek(self):
        self.fill(self.s1, self.s2)
        peeky = self.s2[-1]
        self.fill(self.s2, self.s1)
        return peeky
        

    # @return an boolean
    def empty(self):
        return len(self.s1) == 0
        