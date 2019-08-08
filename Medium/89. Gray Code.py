class Solution:
    def grayCode(self, n: int) -> list:
        if n == 0: return [0]
        self.ans = []
        self.depth = n
        self.recursive(['0','1'], n)
        self.ans = [int(x,2) for x in self.ans]
        return self.ans 
        
    def recursive(self, prefix, n):
        if n == 1:
            self.ans += prefix
            return
        
        rev = prefix.copy()
        rev.reverse()
        
        for i in range(len(prefix)):
            prefix[i] = '0' + prefix[i]
        for i in range(len(rev)):
            rev[i] = '1' + rev[i]
            
        self.recursive(prefix+rev,n-1)