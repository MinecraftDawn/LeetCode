class Solution:
    def productExceptSelf(self, nums: list) -> list:
        ans = [1] * len(nums)
        
        tmp = nums[0]
        for left in range(1,len(nums)):
            ans[left] *= tmp
            tmp *= nums[left]
            
        tmp = nums[-1]
        for right in range(len(nums)-2, -1, -1):
            ans[right] *= tmp
            tmp *= nums[right]
            
        return ans