class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]

        def recursive(start, end):
            if start >= end: return 0
            if dp[start][end]: return dp[start][end]
            
            tmp = float("inf")
            for i in range(start, end+1):
                left = recursive(start, i-1)
                right = recursive(i+1, end)
                tmp = min(tmp, i + max(left,right))
            dp[start][end] = tmp
            
            return dp[start][end]

        return recursive(1, n)