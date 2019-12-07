class Solution:
    def rob(self, nums: list) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        def notCircle(nums):
            pre,cur = 0,0
            
            for num in nums:
                tmp = cur
                cur = max(cur, num+pre)
                pre = tmp
                
            return cur
        
        left = notCircle(nums[:len(nums)-1])
        right = notCircle(nums[1:]) 
        
        return max(left,right)