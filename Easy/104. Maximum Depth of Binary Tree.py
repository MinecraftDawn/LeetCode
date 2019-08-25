# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0
        self.dfs(root, 0)
        return self.depth
    
    def dfs(self, node: TreeNode, depth: int):
        if node:
            self.dfs(node.left, depth+1)
            self.dfs(node.right, depth+1)
        else:
            self.depth = max(self.depth, depth)