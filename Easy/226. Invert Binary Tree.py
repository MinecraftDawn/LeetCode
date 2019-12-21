# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.swapChild(root)
        return root
        
    def swapChild(self, node: TreeNode) -> None:
        if not node: return
        node.left, node.right = node.right, node.left
        self.swapChild(node.left)
        self.swapChild(node.right)