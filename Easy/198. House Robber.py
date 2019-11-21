class Solution:
    def rob(self, nums: list) -> int:
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        
        pre,cur = 0,0
        
        for i in range(len(nums)):
            tmp = cur
            cur = max(cur, nums[i] + pre)
            pre = tmp
        return cur