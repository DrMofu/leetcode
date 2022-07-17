# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd_head = ListNode(next=None)
        even_head = ListNode(next=None)
        odd_pointer = odd_head
        even_pointer = even_head
        counter = 1
        while head:
            if counter%2==1:
                odd_pointer.next = head
                odd_pointer = odd_pointer.next
            else:
                even_pointer.next = head
                even_pointer = even_pointer.next
            head_next = head.next
            head.next = None
            head = head_next
            counter +=1
        odd_pointer.next = even_head.next
        return odd_head.next
                