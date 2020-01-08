# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        if not root: return []
        self.ans = []
        self.dfs(root, [])
        return self.ans
        
    def dfs(self, node: TreeNode, path: list):      
        path.append(str(node.val))
        if not node.left and not node.right:
            self.ans.append("->".join(path))

        if node.left:
            self.dfs(node.left, path)
        if node.right:
            self.dfs(node.right, path)
        path.pop()