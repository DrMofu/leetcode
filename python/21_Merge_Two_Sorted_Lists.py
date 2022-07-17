# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1: return list2
        if not list2: return list1
        if list1.val<list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        list2.next = self.mergeTwoLists(list1,list2.next)
        return list2
    
        # head_node = ListNode()
        # head_pointer = head_node
        # while l1 and l2:
        #     if l1.val<l2.val:
        #         head_pointer.next = l1
        #         head_pointer = head_pointer.next
        #         l1 = l1.next
        #     else:                
        #         head_pointer.next = l2
        #         head_pointer = head_pointer.next
        #         l2 = l2.next
        # if l1:            
        #     head_pointer.next = l1
        # else:            
        #     head_pointer.next = l2
        # return head_node.next