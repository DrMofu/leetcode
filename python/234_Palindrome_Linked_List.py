# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # find middle
        dumb = ListNode(next=head)
        slow = fast = dumb
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow node now is the pre node of reverse list        
        # reverse
        node = slow.next
        tail = None
        while node:
            node_next = node.next
            node.next = tail
            tail = node
            node = node_next 
        
        # compare
        while tail:
            if tail.val!=head.val:
                return False
            tail = tail.next
            head = head.next
        return True