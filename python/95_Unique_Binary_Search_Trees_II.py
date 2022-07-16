# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def genTree(self,start,end): # not include end
        if start>=end: return [None]
        if start==end-1:
            node = TreeNode(val=start)
            return [node]

        results = []
        for root_value in range(start,end):
            left = self.genTree(start,root_value)
            right = self.genTree(root_value+1,end)
            for l in left:
                for r in right:
                    node = TreeNode(val=root_value,left=l,right=r)
                    results.append(node)
        return results
                    
            
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.genTree(1,n+1)
        