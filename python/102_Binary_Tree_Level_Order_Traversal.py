# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        queue = [[root,0]]
        curr_val = []
        curr_level = 0
        while queue:
            node,level = queue.pop(0)
            if level!=curr_level:
                ans.append(curr_val[:])
                curr_level+=1
                curr_val = []
            curr_val.append(node.val)
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
                
        if len(curr_val):
            ans.append(curr_val)
        
        return ans