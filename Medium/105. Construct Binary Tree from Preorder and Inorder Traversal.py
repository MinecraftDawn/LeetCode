# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if not preorder or not inorder: return
        
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        
        return root