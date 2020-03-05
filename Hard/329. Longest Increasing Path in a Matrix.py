class Node:
    def __init__(self, value:int):
        self.value = value
        self.neigh = []

class Solution:
    def longestIncreasingPath(self, matrix: list) -> int:
        if not matrix: return 0
        visted = set()
        
        allNode = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                allNode[row][col] = Node(matrix[row][col])
                
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                cur = matrix[row][col]
                if row-1 >= 0 and matrix[row-1][col] > cur:
                    allNode[row][col].neigh.append(allNode[row-1][col])
                if row+1 < len(matrix) and matrix[row+1][col] > cur:
                    allNode[row][col].neigh.append(allNode[row+1][col])
                if col-1 >= 0 and matrix[row][col-1] > cur:
                    allNode[row][col].neigh.append(allNode[row][col-1])
                if col+1 < len(matrix[0]) and matrix[row][col+1] > cur:
                    allNode[row][col].neigh.append(allNode[row][col+1])
                    
        
        def dfs(node:Node) -> int:
            direct = [0]
            visted.add(node)
            for n in node.neigh:
                if n not in visted:
                    direct.append(dfs(n))
                
            visted.remove(node)
            return max(direct) + 1
        
        maxPath = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                maxPath = max(maxPath, dfs(allNode[row][col]))
                
        return maxPath