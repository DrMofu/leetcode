# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -float("inf")
        def dfs(node):
            if not node:
                return 0
            left_max = dfs(node.left) # must contain node.left
            right_max = dfs(node.right) # must contain node.right
            # must contain current node:
            single_path_max = max([node.val+left_max, node.val+right_max, node.val])
            curr_max_path = max(single_path_max, node.val+left_max+right_max)
            self.max_sum = max(self.max_sum,curr_max_path)
            return single_path_max
        dfs(root)
        return self.max_sum