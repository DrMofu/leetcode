# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        def dfs(node,parent=None):
            if node:
                node.parent=parent
                dfs(node.left,node)
                dfs(node.right,node)
                
        dfs(root)

        queue = [(target,0)]
        done = set([target])

        while queue:
            if queue[0][1]==k:
                return [node.val for node,level in queue]
            node,level = queue.pop(0)
            for neighbor in [node.left,node.right,node.parent]:
                if neighbor and neighbor not in done:
                    done.add(neighbor)
                    queue.append((neighbor,level+1))
        return []