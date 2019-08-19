# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        self.vaild = True
        self.preVal = -99999999999999
        self.inorder(root)
        
        return self.vaild
        
    def inorder(self, node:TreeNode):
        if not node or not self.vaild: return
        
        self.inorder(node.left)
        
        if node.val <= self.preVal:
            self.vaild = False
            return
        
        self.preVal = node.val
        
        self.inorder(node.right) 