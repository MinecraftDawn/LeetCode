class Solution:
    def combinationSum4(self, nums:list, target: int) -> int:
        dp = [1] + [0] * target
        
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[-1]