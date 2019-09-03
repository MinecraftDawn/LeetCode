# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list:
        self.ans = []
        self.dfs(root, sum, [])
        return self.ans
        
        
    def dfs(self, node:TreeNode, curSum:int, array:list):
        if not node: return
        
        curSum -= node.val
        if not node.left and not node.right:
            if curSum == 0:
                self.ans.append(array + [node.val])
        
        array.append(node.val)
        self.dfs(node.left, curSum, array)
        array.pop()
        
        array.append(node.val)
        self.dfs(node.right, curSum,array)
        array.pop()