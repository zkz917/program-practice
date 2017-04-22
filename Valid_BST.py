# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        max_int = sys.maxint
        min_int = -sys.maxint -1
        
        return self.dfs(root,max_int,min_int)
    
    def dfs(self,root, maxval, minval):
        if not root:
            return True
        if root and root.val >= maxval or root.val <= minval:
            return False
        
        return self.dfs(root.left, root.val, minval) and self.dfs(root.right, maxval, root.val)
        
