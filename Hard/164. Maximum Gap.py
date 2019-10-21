class Solution:
    def maximumGap(self, nums: list) -> int:
        if len(nums) < 2: return 0
        
        nums.sort()
        gap = 0
        for i in range(len(nums)-1):
            gap = max(gap, nums[i+1]-nums[i])
            
        return gap