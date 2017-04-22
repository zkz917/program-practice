# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        
        q =[]
        q.append(root)
        while q:
            s = []
            q1 = []
            for r in q:
                s.append(r.val)
                if r.left:
                    q1.append(r.left)
                if r.right:
                    q1.append(r.right)
            result.append(s)
            q = q1
        
        return result
                
                
            
        
