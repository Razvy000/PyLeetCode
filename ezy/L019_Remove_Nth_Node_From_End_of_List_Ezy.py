'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

import ListNode

class L019_Remove_Nth_Node_From_End_of_List_Ezy:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        # create a forward pointer and a sentry
        forward = head
        sentry = ListNode(0)
        sentry.next = head
        curr = sentry
        
        # move a forward pointer
        for _ in range(0, n):
            forward = forward.next
            
        # move both at the same time
        while forward:
            forward = forward.next
            curr = curr.next
            
        # remove element
        curr.next = curr.next.next
        
        return sentry.next
