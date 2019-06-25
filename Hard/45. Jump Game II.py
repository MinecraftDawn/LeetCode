# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:21:09 2019

@author: Eric
"""

class Solution:
    def jump(self, nums: list) -> int:
        if not nums or len(nums) == 1: return 0
        
        dp = [1048576] * len(nums)
        check = [True] * len(nums)
        
        index = 0
        while index < len(nums):
            indexNum = nums[index]
            
            if check[index]:
                for j in range(index+1, index+indexNum+1):
                    if j >= len(nums): continue
                    if indexNum - (j - index) >= nums[j]: check[j] = False
                    
                    dp[j] = min(dp[j], index+1,dp[index]+1)
                    
            index += 1
        return dp.pop()