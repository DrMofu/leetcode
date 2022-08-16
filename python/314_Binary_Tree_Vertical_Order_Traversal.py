# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        my_hash = {}
        queue = [(root,0)]
        while queue:
            node,index = queue.pop(0)
            if node:
                if index not in my_hash:
                    my_hash[index]=[]
                my_hash[index].append(node.val)
                queue.append([node.left,index-1])
                queue.append([node.right,index+1])
        return [my_hash[index] for index in sorted(my_hash.keys())]