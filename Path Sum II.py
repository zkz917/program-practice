# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        Solution.res = []
        self.dfs(root,sum,[])
        return Solution.res
    def dfs(self,root,sum,temp):
        if not root:
            return []
        if sum == root.val and not root.left and not root.right:
            temp.append(root.val)
            Solution.res.append(temp)
        self.dfs(root.left, sum - root.val, temp + [root.val])
        self.dfs(root.right, sum - root.val, temp + [root.val])
        
