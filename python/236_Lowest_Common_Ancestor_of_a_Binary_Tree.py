# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {}
        def dfs(node):
            if not node:
                return
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        
        dfs(root)
        p_ancestor = [p.val]
        while p in parent:
            p = parent[p]
            p_ancestor.append(p.val)
            
        q_ancestor = [q]
        while q in parent:
            q = parent[q]
            q_ancestor.append(q)
            
            
        p_ancestor = set(p_ancestor)
        for node in q_ancestor:
            if node.val in p_ancestor:
                return node
            
