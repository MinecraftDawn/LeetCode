class Solution:        
    def numTrees(self, n: int) -> int:
        return self.recursive(n)
    
    def recursive(self, n):
        if n == 0: return 1
        
        m = n-1
        return (4*m+2)*self.recursive(m) // (m+2)