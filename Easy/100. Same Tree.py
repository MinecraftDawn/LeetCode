# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.valid = True
        self.dfs(p, q)
        return self.valid
    
    def dfs(self, p:TreeNode, q:TreeNode) -> None:
        if p and q:
            if self.valid:
                if p.val == q.val:
                    self.dfs(p.left, q.left)
                    self.dfs(p.right, q.right)
                else:
                    self.valid = False
        elif not p and not q:
            pass
        else:
            self.valid = False