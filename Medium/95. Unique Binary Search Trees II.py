# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> list:
        if n == 0: return []
        return self.generate(1,n)
    
    def generate(self, left, right):
        if right < left: return [None]
        
        tree = []
        for i in range(left, right+1):
            for leftTree in self.generate(left, i-1):
                for rightTree in self.generate(i+1, right):
                    root = TreeNode(i)
                    root.left = leftTree
                    root.right = rightTree
                    tree.append(root)
                    
        return tree if tree else [None]