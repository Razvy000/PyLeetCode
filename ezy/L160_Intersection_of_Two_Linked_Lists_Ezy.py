'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                                                       ↘
                     c1 → c2 → c3
                                                       ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''


class L160_Intersection_of_Two_Linked_Lists_Ezy:
    
    # @param two ListNodes
    # @return the intersected ListNode
    
    # get the lengths, move the longest diff steps and then step both at same time
    def getIntersectionNode(self, headA, headB):
        l1 = self.lenL(headA)
        l2 = self.lenL(headB)
        
        # move the longest diff steps
        if l1 < l2:
            for _ in range(l2 - l1):
                headB = headB.next
        elif l1 > l2:
            for _ in range(l1 - l2):
                headA = headA.next
        
        # step both at the same time
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA
        
    def lenL(self, head):
        s = 0
        while not head is None:
            s += 1
            head = head.next
        return s