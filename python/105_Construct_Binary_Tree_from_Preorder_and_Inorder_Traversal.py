# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inorder_index = {}
        for i,val in enumerate(inorder):
            inorder_index[val]=i
        
        self.preorder_index = 0
        
        def generate_tree(left,right):
            if left>right:
                return None
                
            node_val = preorder[self.preorder_index]
            node = TreeNode(node_val)
            self.preorder_index+=1
            
            node.left = generate_tree(left,inorder_index[node_val]-1)
            node.right = generate_tree(inorder_index[node_val]+1,right)
            
            return node
        
        
        return generate_tree(0,len(preorder)-1)