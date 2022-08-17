"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
        # save global parameters here!
        self.already_have = {}
    
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        
        if node.val in self.already_have:
            return self.already_have[node.val]
        
        clone_node = Node(val=node.val)
        self.already_have[node.val] = clone_node # save before get neighbors
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        return clone_node