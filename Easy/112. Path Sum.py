# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        
        if not root.left and not root.right:
            sum -= root.val
            if sum == 0: return True
            else: return False
            
        elif not root.left:
            sum -= root.val
            return self.hasPathSum(root.right, sum)
        
        elif not root.right:
            sum -= root.val
            return self.hasPathSum(root.left, sum)
        
        else:
            sum -= root.val
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)