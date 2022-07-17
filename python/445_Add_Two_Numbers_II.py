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
        left = []
        right = []
        while l1:
            left.append(l1.val)
            l1 = l1.next
        while l2:
            right.append(l2.val)
            l2 = l2.next
        
        head = None
        carry = 0
        while left or right or carry!=0:
            a = 0 if not left else left.pop()
            b = 0 if not right else right.pop()
            sum_val = a+b+carry
            carry=sum_val//10
            sum_val = sum_val%10
            node = ListNode(sum_val)
            node.next = head
            head = node
        return head