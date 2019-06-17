class Solution:
    def jump(self, nums: list) -> int:
        if not nums or len(nums) == 1: return 0
        
        dp = [1048576] * len(nums)
        
        for index,indexNum in enumerate(nums):
            for j in range(index, index+indexNum+1):
                if j >= len(nums): continue
                if j == 5: print(index,indexNum,j)
                dp[j] = min(dp[j], index+1,dp[index]+1)
                
        return dp.pop()