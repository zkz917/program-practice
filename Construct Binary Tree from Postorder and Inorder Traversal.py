class Solution(Object):
  def buildTrees(self, inorder, postorder):
    
    if inorder:
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        root.left = self.buildTrees(inorder[0:ind], postorder[0:ind])
        root.right = self.buildTrees(inorder[ind+1:], postorder[ind:])
        
        return root
