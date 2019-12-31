# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = []
        self.dfs(root, p, pPath, [])
        
        qPath = []
        self.dfs(root, q, qPath, [])
        
        for i in qPath[::-1]:
            if i in pPath:
                return i

    
    def dfs(self, node: 'TreeNode', target: 'TreeNode', path: list, find: list) -> None:
        if not node: return
        
        path.append(node)
        if node != target:
            self.dfs(node.left, target, path, find)
            
            if not find:
                self.dfs(node.right, target, path, find)
            
        else:
            find.append(True)
            
        if not find:
            path.pop()