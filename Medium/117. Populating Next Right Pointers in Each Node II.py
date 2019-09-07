"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [[],[]]
        queue[0].append(root)
        
        while queue[0]:
            node = queue[0].pop(0)
            
            if node.left:
                queue[1].append(node.left)
            if node.right:
                queue[1].append(node.right)
                
            if not queue[0]:
                queue[0],queue[1] = queue[1],queue[0]
            else:
                node.next = queue[0][0]
                
        return root