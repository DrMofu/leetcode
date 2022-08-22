# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
#     # method 1: binary tree
#     def __init__(self):
#         # global variable
#         self.previous = None
#         self.inorder_successor_node = None
    
#     def inorder(self,node,p):
#         if not node or self.inorder_successor_node:
#             return
        
#         # Recurse on the left side
#         self.inorder(node.left, p)
        
#         # Check if previous is the inorder predecessor of node
#         if self.previous == p and not self.inorder_successor_node:
#             self.inorder_successor_node = node
#             return
        
#         # Keeping previous up-to-date for further recursions
#         self.previous = node
        
#         # Recurse on the right side
#         self.inorder(node.right, p)
        
#     def inorderSuccessor(self, root, p):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :rtype: TreeNode
#         """
        
#         self.inorder(root,p)
#         return self.inorder_successor_node
    
    # method 2: BST
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        node = root
        successor = None
        while node:
            if p.val>=node.val:
                node = node.right
            else:
                successor = node
                node = node.left
        return successor