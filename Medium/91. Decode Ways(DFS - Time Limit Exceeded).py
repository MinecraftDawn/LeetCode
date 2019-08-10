class Solution:
    def numDecodings(self, s: str) -> int:
        self.ans = 0
        self.dfs(s)
        return self.ans
    
    def dfs(self, s):
        if len(s) == 0: 
            self.ans += 1
        elif len(s) == 1:
            if s[0] == '0': return
            self.ans += 1
        else:
            if s[0] == '0': return
            
            if int(s[:2]) <= 26:
                self.dfs(s[2:])
            self.dfs(s[1:])