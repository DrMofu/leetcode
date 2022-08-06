# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev_node = header = ListNode()
        c = 0
        while l1 or l2 or c:
            l1_value = 0
            l2_value = 0
            if l1:
                l1_value = l1.val
                l1 = l1.next
            if l2:
                l2_value = l2.val
                l2 = l2.next
            val = l1_value+l2_value+c
            c=val//10
            val = val%10
            new_node = ListNode(val=val)
            prev_node.next = new_node
            prev_node = new_node
            
        return header.next