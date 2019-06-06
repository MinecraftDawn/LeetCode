class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        length = len(nums)
        
        if not length: return [-1,-1]
        
        ans = []
        first = 0
        end = length - 1
        mid = -1
        
        while first <= end:
            mid = (first + end) // 2
            
            if nums[mid] == target:
                break
            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    first = mid + 1
        if nums[mid] != target:
            mid = -1
        
        left = mid - 1
        right = mid + 1
        while left >= 0:
            if nums[left] == target:
                left -= 1
            else:
                break
            
        while right < length:
            if nums[right] == target:
                right += 1
            else:
                break
            
        ans.append(left+1)
        ans.append(right-1)
        return ans