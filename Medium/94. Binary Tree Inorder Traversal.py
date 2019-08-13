# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        self.ans = []
        self.inorder(root)
        
        return self.ans
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            self.ans.append(node.val)
            self.inorder(node.right)