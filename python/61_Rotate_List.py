# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        list_len =0
        dumb_node = ListNode(next=head)
        end_node = dumb_node
        while end_node.next:
            list_len+=1
            end_node=end_node.next
        if list_len==0:
            return head
            
        # now, the problem become find nth pos from the last
        rotate_pos = list_len-(k%list_len)
        end_node.next = head # become circle
        pre_new_head = dumb_node
        for i in range(rotate_pos):
            pre_new_head = pre_new_head.next
        new_head = pre_new_head.next
        pre_new_head.next = None # remove circle
        return new_head
        
        
        