class Solution:
    def maxEnvelopes(self, envelopes: list) -> int:
        if len(envelopes) < 2:
            return len(envelopes)
        
        envelopes.sort()
        ans = 1
        dp = [1 for _ in range(len(envelopes))]
        
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and \
                envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            
            ans = max(ans, dp[i])
        return ans