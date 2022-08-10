# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l ==0:
            return None
        mid=int(l/2)
        this_node = TreeNode()
        this_node.val = nums[mid]
        this_node.left = self.sortedArrayToBST(list(nums[:mid]))
        this_node.right = self.sortedArrayToBST(list(nums[mid+1:]))
        return this_node
        