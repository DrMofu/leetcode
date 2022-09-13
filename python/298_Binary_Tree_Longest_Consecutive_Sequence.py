# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,prev_sum):
            max_ans = prev_sum
            if not node:
                return 0
            if node.left:
                if node.left.val==node.val+1:
                    max_ans = max(max_ans,dfs(node.left,prev_sum+1))
                else:
                    max_ans = max(max_ans,dfs(node.left,1))
            if node.right:
                if node.right.val==node.val+1:
                    max_ans = max(max_ans,dfs(node.right,prev_sum+1))
                else:
                    max_ans = max(max_ans,dfs(node.right,1))
            return max_ans
        
        return dfs(root,1)
        
        