# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balance = True
        
        self.dfs(root, 0)
        
        return self.balance
    
    def dfs(self, node, depth):
        if node:
            leftVal = self.dfs(node.left, depth+1) + 1
            rightVal = self.dfs(node.right, depth+1) + 1
            
            if abs(leftVal - rightVal) > 1:
                self.balance = False
        
            return max(leftVal,rightVal)
        else:
            return 0