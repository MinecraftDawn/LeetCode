class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if not nums: return []
        ans = []
        queue = []
        
        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        
        for i in range(k, len(nums)):
            ans.append(queue[0])
            if nums[i-k] == queue[0]:
                queue.pop(0)
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        ans.append(queue[0])
        
        return ans