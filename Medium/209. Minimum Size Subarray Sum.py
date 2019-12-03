class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
        left = 0
        curNum = 0
        minSize = float('inf')
        
        for right in range(len(nums)):
            curNum += nums[right]
            
            while curNum >= s:
                minSize = min(minSize, right - left + 1)
                curNum -= nums[left]
                left += 1
                
        return minSize if minSize != float('inf') else 0