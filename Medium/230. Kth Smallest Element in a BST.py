# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.ans = root
        self.inorder(root)
        return self.ans.val
    
    def inorder(self, node:TreeNode):
        if not node: return
        
        self.inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.ans = node
        elif self.k > 0:
            self.inorder(node.right)