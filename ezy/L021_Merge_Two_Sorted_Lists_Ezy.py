'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''

import ListNode

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    
    # idea: use a sentry/dummy
    def mergeTwoLists(self, l1, l2):
        sentry = ListNode(0)
        l = sentry
        
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
          
        # append remaining list  
        if l1:
            l.next = l1
        elif l2:
            l.next = l2
            
        return sentry.next