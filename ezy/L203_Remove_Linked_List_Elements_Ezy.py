'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

import ListNode

class L203_Remove_Linked_List_Elements_Ezy:
    
    
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements2(self, head, val):
        if not head:
            return None
        if head.val == val:
            return self.removeElements(head.next, val)
        head.next = self.removeElements(head.next, val)
        return head
        
        
    def removeElements(self, head, val):
        if not head:
            return None
        
        sentry = ListNode(0)
        q = sentry
        p = head
        while p:
            if p.val != val:
                q.next = p
                q = q.next
            p = p.next
            
        q.next = None    
        
        return sentry.next
    