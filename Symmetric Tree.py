# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isS(root.left, root.right)
        
    def isS(self, left,right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.isS(left.left,right.right) and self.isS(left.right,right.left)
