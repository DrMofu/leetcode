import collections
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
        :rtype: int
        """
        pre_sum = collections.defaultdict(int)
        pre_sum[0]=1
        def dfs(node,curr_sum):
            if not node:
                return 0
            
            curr_sum+=node.val
            ans = pre_sum[curr_sum-targetSum]
            pre_sum[curr_sum]+=1           
            
            ans+=dfs(node.left,curr_sum)
            ans+=dfs(node.right,curr_sum)
            pre_sum[curr_sum]-=1
            
            # print(curr_sum,curr_sum-targetSum,pre_sum[curr_sum-targetSum])
            return ans
        
        
        return dfs(root,0)