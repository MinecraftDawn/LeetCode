class Solution:
    def __init__(self):
        self.dict = {}
           
    def numTrees(self, n: int) -> int:
        return self.recursive(n)
    
    def recursive(self, n):
        if n == 0: return 1
        m = n-1
        
        dictVal = self.dict.get(m)
        if dictVal:
            return dictVal
        
        else:
            num = (4*m+2)*self.recursive(m) // (m+2)
            self.dict[m] = num
            return num