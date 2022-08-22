# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_list(head,k):
            tail = None
            node = head
            for i in range(k):
                node_next = node.next
                node.next= tail
                tail = node
                node = node_next
            return tail,head            
        
        dump_node = ListNode(next=head)
        pre_list_node = dump_node
        after_list_node = head
        while after_list_node:
            reach_end = False
            for i in range(k):
                if after_list_node:
                    after_list_node = after_list_node.next
                else:
                    # finish reverse
                    reach_end = True
                    break
            if not reach_end:
                new_head,new_tail = reverse_list(pre_list_node.next,k)
                pre_list_node.next = new_head
                new_tail.next = after_list_node
                pre_list_node = new_tail
                    
        return dump_node.next