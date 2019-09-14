# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPath = -2e30
        self.dfs(root)
        return self.maxPath
    
    def dfs(self, node:TreeNode) -> int:
        if not node: return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        curMaxPath = max(node.val, left+node.val, right+node.val)
        includeNodePath = max(curMaxPath, node.val+left+right)
        self.maxPath = max(self.maxPath, includeNodePath)
        return curMaxPath