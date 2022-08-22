# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    def inorder(self,node):
        if not node:
            return
        self.inorder(node.left)
        self.inorder_list.append(node.val)
        self.inorder(node.right)
        
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.inorder_list = []
        self.inorder(root)
        self.len = len(self.inorder_list)
        self.pointer = 0
        

    def next(self):
        """
        :rtype: int
        """
        ans = self.inorder_list[self.pointer]
        self.pointer+=1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointer<self.len
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()