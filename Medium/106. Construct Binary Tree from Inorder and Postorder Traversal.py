# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if not postorder or not inorder: return
        
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:index],postorder[:index])
        root.right = self.buildTree(inorder[index+1:],postorder[index:-1])
        
        return root