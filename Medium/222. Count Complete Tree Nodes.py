# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.nodesNum = 0
        
        def dfs(node: TreeNode) -> None:
            if not node: return
            self.nodesNum += 1
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.nodesNum