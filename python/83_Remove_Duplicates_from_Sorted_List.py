# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head_node = ListNode(next=head)
        # unique_node_start = head
        # while unique_node_start:
        #     unique_node_end = unique_node_start.next
        #     while unique_node_end and unique_node_end.val == unique_node_start.val:
        #         unique_node_end = unique_node_end.next
        #     unique_node_start.next = unique_node_end
        #     unique_node_start = unique_node_start.next
        # return head_node.next
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val==head.next.val:
            return head.next
        return head