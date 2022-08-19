# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find middle
        dumb = ListNode(next=head)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now, slow_val = n//2+1
        
        # reverse
        tails = None
        curr = slow
        while curr:
            curr_next = curr.next
            curr.next = tails
            tails = curr
            curr = curr_next
            
        # combine tails and old head
        first = head
        second = tails
        
        while second.next!=None:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next        
        
        return dumb.next