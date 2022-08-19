# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        for node in lists:
            if not node:
                continue
            heapq.heappush(min_heap,(node.val,node))
        
        head = ListNode()
        pointer = head
        while min_heap:
            val,node = heapq.heappop(min_heap)
            pointer.next = node
            pointer = node
            if node.next:
                node = node.next
                heapq.heappush(min_heap,(node.val,node))
                
        return head.next