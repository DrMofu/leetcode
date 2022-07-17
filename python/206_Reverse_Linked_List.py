# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # method 1
        prev_node = None
        while head:
            head_next = head.next
            head.next = prev_node
            prev_node = head
            head = head_next
        return prev_node
        
        # # method 2
        # if not head or not head.next:
        #     return head
        # head_next = head.next
        # new_head = self.reverseList(head_next)
        # head_next.next = head
        # head.next = None
        # return new_head