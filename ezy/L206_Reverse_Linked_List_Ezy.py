'''
Reverse a singly linked list.
 
Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

import ListNode

class L206_Reverse_Linked_List_Ezy:
    
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList2(self, head):
        l = None
        while not head == None:
            l2 = ListNode(head.val)
            l2.next = l
            l = l2
            head = head.next
        return l
    
    # in place
    def reverseList22(self, head):
        newHead = None
        while not head == None:
            nexte = head.next
            head.next = newHead
            newHead = head
            head = nexte
        return newHead
    
    # recursive new list
    def reverseList(self, head):
        if head == None:
            return head
        
        return self.revHelp(head)[0]
    
    def revHelp(self, head):
        if head.next == None:
            l2 = ListNode(head.val)
            return (l2, l2)
            
        rev, last = self.revHelp(head.next)
        last.next = ListNode(head.val)
        return (rev, last.next)    
    
    # recursive 2, in place
    def reverseList3(self, head, last=None):
        if not head:
            return last
        nexte = head.next
        head.next = last
        return self.reverseList3(nexte, head)
