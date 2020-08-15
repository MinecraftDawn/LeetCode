class Solution:
    def canPartition(self, nums: list) -> bool:
        s = sum(nums)
        if s % 2: return False

        dp = [[False for _ in range(s // 2 + 1)] for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(s // 2 + 1):
                cur = nums[i - 1]
                if cur <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - cur]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]