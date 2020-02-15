class Solution:
    def findMinHeightTrees(self, n: int, edges: list) -> list:
        if not edges: return [0]
        
        path = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        
        for p1,p2 in edges:
            path[p1].append(p2)
            path[p2].append(p1)
            degree[p1] += 1
            degree[p2] += 1
        
        queue = [[],[]]

        for i in range(n):
            if degree[i] == 1:
                queue[0].append(i)
                
                
        while n > 2:
            while queue[0]:
                left = queue[0].pop(0)
                n -= 1
                
                for j in path[left]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        queue[1].append(j)
                        
            if not queue[0]:
                queue[0],queue[1] = queue[1],queue[0]
        
        return queue[0]