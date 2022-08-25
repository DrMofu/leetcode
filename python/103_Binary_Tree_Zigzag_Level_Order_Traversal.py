# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        
        queue = [root]
        level = 0
        while queue:
            tmp = []
            next_queue = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if level%2==0:
                ans.append(tmp[:])
            else:
                ans.append(tmp[::-1])
            level+=1        
            queue = next_queue
        return ans