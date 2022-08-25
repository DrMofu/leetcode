# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root,0)]
        max_width = 0
        while queue:
            next_queue = []
            width = queue[-1][1] - queue[0][1]+1
            max_width = max(max_width,width)
            for node,index in queue:
                if node.left:
                    next_queue.append((node.left,2*index))
                if node.right:
                    next_queue.append((node.right,2*index+1))
                    
            queue = next_queue
        return max_width