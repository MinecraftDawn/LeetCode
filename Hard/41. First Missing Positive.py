import heapq
class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        ans = 1
        heapq.heapify(nums)
        
        for i in range(len(nums)):
            pop = heapq.heappop(nums)
            if pop == ans: ans += 1
            elif pop > ans: break
        return ans