# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node,lower,upper):
            if not node:
                return True
            if node.val<=lower or node.val>=upper:
                return False
            return dfs(node.left,lower,min(upper,node.val)) and dfs(node.right,max(lower,node.val),upper)
        
        return dfs(root,-float("inf"),float("inf"))
                