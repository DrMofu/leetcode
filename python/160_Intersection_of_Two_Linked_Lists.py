# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # a + c + b = b + c + a
        l1 = headA
        l2 = headB
        while l1!=l2:
            if not l1:
                l1 = headB
            else:
                l1 = l1.next
            if not l2:
                l2 = headA
            else:
                l2 = l2.next
        return l1