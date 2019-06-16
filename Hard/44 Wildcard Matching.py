class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        i = 0 
        while i < len(p)-1:
            if p[i] == p[i+1] == '*':
                p = p[:i] + p[i+1:]
            else:
                i += 1
                
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        
        if p and p[0] == '*': dp[-1][0] = True
          
        for si in range(len(s)):
            char = s[si]
            
            for pi in range(len(p)):
                patten = p[pi]
                if patten == char or patten == '?':
                    dp[si][pi] = dp[si-1][pi-1]
                elif patten == '*':
                    dp[si][pi] = dp[si-1][pi-1] or dp[si-1][pi] or dp[si][pi-1]
                else:
                    dp[si][pi] = False
         
        return dp[len(s)-1][len(p)-1]