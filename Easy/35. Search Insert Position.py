class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        length = len(nums)
        
        if not length: return 0
        
        first = 0
        end = length - 1
        mid = -1
        
        if nums[first] >= target:
            return 0
        
        if nums[end] < target:
            return end+1
        
        while first <= end:
            mid = (first + end) // 2
            
            if nums[mid] == target:
                break
            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    first = mid + 1
                    mid = first
        
        return mid