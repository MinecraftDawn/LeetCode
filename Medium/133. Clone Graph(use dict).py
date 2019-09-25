"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visted = {}
        return self.dfs(node)
        
    def dfs(self, node: 'Node') -> 'Node':
        vistedNeig = self.visted.get(node.val)
        if vistedNeig:
            return vistedNeig
        
        neighbors = []
        newNode = Node(node.val, [])
        self.visted[node.val] = newNode
        for i in node.neighbors:
            neighbors.append(self.dfs(i))
            
        newNode.neighbors = neighbors
        
        return newNode  