# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result_list = []
        current_nodes = []
        
        def backtrack(node):
            if not node.left and not node.right:
                # save result:
                result_string = str(root.val)
                for item in current_nodes[1:]:
                    result_string += "->"
                    result_string += str(item.val)
                result_list.append(result_string)
                return
            if node.left:
                current_nodes.append(node.left)
                backtrack(node.left)
                current_nodes.pop()
            
            if node.right:
                current_nodes.append(node.right)
                backtrack(node.right)
                current_nodes.pop()
            
        current_nodes.append(root)
        backtrack(root)
        return result_list