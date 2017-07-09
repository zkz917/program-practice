# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # use bfs to do the level order travesal and connect the node in the queue
    def connect(self, root):
        if not root:
            return 
        q = [root]
        while q:
            l = len(q)
            for i in range(l-1):
                q[i].next = q[i+1]
            for i in range(l):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        