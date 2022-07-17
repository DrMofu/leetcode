# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        before_head = ListNode(next = head)
        
        pre_node = before_head
        while pre_node.next and pre_node.next.next:            
            left_node = pre_node.next
            right_node = pre_node.next.next
            
            pre_node.next = right_node
            left_node.next = right_node.next
            right_node.next = left_node
            
            pre_node = left_node
        return before_head.next
    
        # if not head or not head.next:
        #     return head
        # newHead = head.next
        # head.next = self.swapPairs(newHead.next)
        # newHead.next = head
        # return newHead

            