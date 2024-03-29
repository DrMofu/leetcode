"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            tmp = []
            next_queue = []
            for node in queue:
                tmp.append(node.val)
                for child in node.children:
                    next_queue.append(child)
            ans.append(tmp)
            queue = next_queue
        return ans