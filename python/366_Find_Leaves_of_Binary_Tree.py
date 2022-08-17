# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def is_leaf(self,node):
        if node and not node.left and not node.right:
            return True
        return False
    
    def dfs(self,node):
        if not node:
            return []
        ans = []
        if self.is_leaf(node.left):
            ans.append(node.left.val)
            node.left = None
        else:
            ans.extend(self.dfs(node.left))
        
        if self.is_leaf(node.right):
            ans.append(node.right.val)
            node.right = None
        else:
            ans.extend(self.dfs(node.right))
        return ans
    
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        head = TreeNode(left=root)
        while head.left:
            ans.append(self.dfs(head))
        return ans