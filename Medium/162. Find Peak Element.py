class Solution:
    def findPeakElement(self, nums: list) -> int:
        if len(nums) <= 3: return nums.index(max(nums))
        
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
        
        return nums.index(max(nums))