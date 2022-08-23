# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node,curr_sum):
            if not node:
                return False
            curr_sum+=node.val            
            if curr_sum==targetSum and not node.left and not node.right:
                return True
            return dfs(node.left,curr_sum) or dfs(node.right,curr_sum)
        
        
        return dfs(root,0)