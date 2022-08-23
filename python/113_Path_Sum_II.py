# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans = []
        tmp = []
        def dfs(node,curr_sum):
            if not node:
                return
            curr_sum+=node.val
            tmp.append(node.val)
            if curr_sum==targetSum and not node.left and not node.right:
                ans.append(tmp[:])
            dfs(node.left,curr_sum)
            dfs(node.right,curr_sum)
            tmp.pop(-1)
        
        dfs(root,0)
        return ans
            