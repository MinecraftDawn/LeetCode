# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return
        
        self.queue = []
        self.inorder(root)
        
        while len(self.queue) > 1:
            pre = self.queue[0]
            nxt = self.queue[1]
            pre.left = None
            pre.right = nxt
            self.queue.pop(0)
        
            
    def inorder(self, node:TreeNode) -> list:
        if not node: return
        
        self.queue.append(node)
        self.inorder(node.left)
        self.inorder(node.right)