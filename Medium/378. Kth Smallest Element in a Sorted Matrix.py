import heapq
class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        
        visted = [[False] * col for _ in range(row)]
        heap = [(matrix[0][0],0,0)]
        
        val = None
        for i in range(k):
            val,r,c = heapq.heappop(heap)
            
            if r+1 < row and not visted[r+1][c]:
                heapq.heappush(heap, (matrix[r+1][c],r+1,c))
                visted[r+1][c] = True
            
            if c+1 < col and not visted[r][c+1]:
                heapq.heappush(heap, (matrix[r][c+1],r,c+1))
                visted[r][c+1] = True
                
        return val