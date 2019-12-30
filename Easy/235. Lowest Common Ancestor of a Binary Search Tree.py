# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodeSet = set(self.bs(root,p.val))
        
        for node in self.bs(root,q.val)[::-1]:
            if node in nodeSet:
                return node
        
        return None
        
    def bs(self, node: 'TreeNode', value: int) -> list:
        if value < node.val:
            return [node] + self.bs(node.left, value)
        elif value >node.val:
            return [node] + self.bs(node.right, value)
        else:
            return [node]