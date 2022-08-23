# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.counter = 0
        self.ans = None
        
    def inorder(self,node,k):
        if not node or self.ans:
            return
        self.inorder(node.left,k)
        # node
        self.counter+=1
        if self.counter==k:
            self.ans = node.val
            return
        self.inorder(node.right,k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
            
        self.inorder(root,k)
        return self.ans
            
        