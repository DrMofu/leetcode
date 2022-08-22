# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        
        node = root
        while node:
            if node.val<val:
                if not node.right:
                    node.right=new_node
                    return root
                node=node.right
            else:
                if not node.left:
                    node.left=new_node
                    return root
                node=node.left
                
        return new_node