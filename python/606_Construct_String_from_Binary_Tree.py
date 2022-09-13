# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.ans = ""
        def dfs(node):
            if not node:
                return
            
            self.ans+=str(node.val)
            if node.right:
                self.ans+="("
                dfs(node.left)
                self.ans+=")"
                self.ans+="("
                dfs(node.right)
                self.ans+=")"
            elif node.left:
                self.ans+="("
                dfs(node.left)
                self.ans+=")"
                
            
        dfs(root)
        return self.ans