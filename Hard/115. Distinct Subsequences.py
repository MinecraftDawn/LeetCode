class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen = len(s)
        tLen = len(t)
        if sLen < tLen: return 0 
        dp = [[0] * (sLen+1) for _ in range(tLen+1)]
        
        for i in range(len(dp[0])):
            dp[0][i] = 1
        
        for i in range(1, sLen+1):
            for j in range(1, tLen+1):
                dp[j][i] = dp[j][i-1]
                if s[i-1] == t[j-1]:
                    dp[j][i] += dp[j-1][i-1]
        
        return dp[-1][-1]