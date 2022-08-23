# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
#     # method 1
#     def exactSub(self,root,subRoot):
#         if not root and not subRoot:
#             return True
#         if not root or not subRoot:
#             return False
#         if root.val==subRoot.val:
#             return self.exactSub(root.left,subRoot.left) and self.exactSub(root.right,subRoot.right)
#         return False
    
#     def isSubtree(self, root, subRoot):
#         """
#         :type root: TreeNode
#         :type subRoot: TreeNode
#         :rtype: bool
#         """
#         if not root and not subRoot:
#             return True
#         if not root or not subRoot:
#             return False
#         if root.val==subRoot.val:
#             if self.exactSub(root.left,subRoot.left) and self.exactSub(root.right,subRoot.right):
#                 return True
#         return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    
    # method 2
    # preorder
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def preorder(node):
            if not node:
                return ["n"]
            ans = [str(node.val)]
            ans += preorder(node.left)
            ans += preorder(node.right)
            return ans
        
        root_str = "_"+"_".join(preorder(root))+"_"
        subRoot_str = "_"+"_".join(preorder(subRoot))+"_"
        print(root_str,subRoot_str)
        return subRoot_str in root_str