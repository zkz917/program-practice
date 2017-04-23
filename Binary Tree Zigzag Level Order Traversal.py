# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        res = []
        q = [root]
        count = 1
        
        while q:
            l = []
            for i in range(len(q)):
                node = q.pop(0)
                l.append(node.val)
                if node.left:
                    # l.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    # l.append(node.right.val)
                    q.append(node.right)
            if count %2 == 0:
                res.append(l[::-1])
            else:
                res.append(l)
            count +=1
        return res
                
