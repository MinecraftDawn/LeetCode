import heapq
class Solution:
    def longestConsecutive(self, nums: list) -> int:
        if not nums: return 0
        
        heapq.heapify(nums)
        ans = 1
        preNum = 2e30
        
        count = 1
        
        while nums:
            num = heapq.heappop(nums)
            if num - preNum == 1:
                count += 1
                ans = max(ans,count)
            elif num == preNum:
                pass
            else:
                count = 1
            preNum = num
                
        return ans