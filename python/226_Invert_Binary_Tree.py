# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def reverse_node(node):
            if not node:
                return
            reverse_node(node.left)
            reverse_node(node.right)
            node.left,node.right = node.right,node.left
            return node
        
        return reverse_node(root)