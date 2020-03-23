# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.dfs(root)[1]
    
    def dfs(self, node:TreeNode) -> int:
        if not node: return (0, 0)
        
        preLeft, maxLeft = self.dfs(node.left)
        preRight, maxRight = self.dfs(node.right)
        
        preMoney = maxLeft + maxRight
        
        curMoney = node.val + preLeft + preRight
        
        return (preMoney, max(preMoney, curMoney))