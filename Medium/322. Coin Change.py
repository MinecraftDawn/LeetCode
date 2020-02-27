class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        dp = [0] + [float("inf")] * (amount)
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i-coin]+1, dp[i])
                
        return dp[-1] if dp[-1] != float("inf") else -1