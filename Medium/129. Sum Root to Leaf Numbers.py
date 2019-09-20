# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.dfs(root, "")
        return self.ans
        
    def dfs(self, node:TreeNode, curNum:str):
        if not node.left and not node.right:
            self.ans += int(curNum + str(node.val))
        elif not node.left:
            self.dfs(node.right, curNum + str(node.val))
        elif not node.right:
            self.dfs(node.left, curNum + str(node.val))
        else:
            self.dfs(node.left, curNum + str(node.val))
            self.dfs(node.right, curNum + str(node.val))