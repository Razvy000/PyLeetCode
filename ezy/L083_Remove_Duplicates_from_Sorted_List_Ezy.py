'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

import ListNode

class L083_Remove_Duplicates_from_Sorted_List_Ezy:
    
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        sentry = ListNode(0)
        sentry.next = head
        
        p = sentry.next
        prev = sentry.next
        
        while p:
            if p.val == prev.val:
                p = p.next
                continue
            
            prev.next = p
            prev = p
            p = p.next
        
        if prev:    
            prev.next = p
        
        return sentry.next
    
