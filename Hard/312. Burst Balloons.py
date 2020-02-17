#Reference: https://www.cnblogs.com/grandyang/p/5006441.html
class Solution:
    def maxCoins(self, nums: list) -> int:
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in range(len(nums))]
        
        for right in range(1, len(nums)-1):
            for left in range(1, len(nums)-right):
                j = left + right - 1
                for k in range(left, j+1):
                    dp[left][j] = max(dp[left][j], nums[left-1]*nums[k]*nums[j+1] + dp[left][k-1] + dp[k+1][j])
        
        return dp[1][len(nums)-2]