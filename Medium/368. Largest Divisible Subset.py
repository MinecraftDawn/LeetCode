class Solution:
    def largestDivisibleSubset(self, nums: list) -> list:
        if not nums: return None
        
        nums.sort()
        dp = [[num] for num in nums]
        
        for indexS in range(len(nums)):
            small = nums[indexS]
            
            
            for indexB in range(indexS+1, len(nums)):
                big = nums[indexB]
                
                if big % small == 0:
                    if len(dp[indexS])+1 > len(dp[indexB]):
                        dp[indexB] = [nums[indexB]] + dp[indexS]
                    
        return max(dp, key=lambda x: len(x))