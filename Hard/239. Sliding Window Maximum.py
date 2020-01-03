class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if not nums: return []
        
        ans = []
        for i in range(len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
        return ans