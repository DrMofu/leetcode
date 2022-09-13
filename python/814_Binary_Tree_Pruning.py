# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return False
            
            left_ans = dfs(node.left)  
            right_ans = dfs(node.right)
            
            if not left_ans:
                node.left = None
                
            if not right_ans:
                node.right = None
                
            
            return (node.val==1) | left_ans | right_ans
    
        
        return root if dfs(root) else None