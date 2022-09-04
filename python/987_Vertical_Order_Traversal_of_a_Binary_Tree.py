# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        queue = collections.deque([(root,0,0)])
        ans_hash = collections.defaultdict(list)
        min_pos = 0
        max_pos = 0
        while queue:
            node,level,pos = queue.popleft()
            ans_hash[pos].append((level,node.val))
            min_pos = min(min_pos,pos)
            max_pos = max(max_pos,pos)
            if node.left:
                queue.append((node.left,level+1,pos-1))
            if node.right:
                queue.append((node.right,level+1,pos+1))
                
                
        ans = []
        for pos in range(min_pos,max_pos+1):
            ans_hash[pos].sort()
            ans.append([item[1] for item in ans_hash[pos]])
        return ans