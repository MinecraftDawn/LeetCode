class Solution:
    def search(self, nums: list, target: int) -> int:
        if not nums: return -1
        
        length = len(nums)
        first = [nums[0],0]
        end = [nums[length-1],length-1]
        while first[0] >= end[0]:
            midIndex = (first[1]+end[1]) // 2
            mid = [nums[midIndex],midIndex]
            
            if mid[0] <= end[0]:
                end = mid.copy()
            if mid[0] >= first[0]:
                first = mid.copy()
            if end[1] - first[1] <= 1:
                break
        
        rotate = first[1] + 1 if first[1] != 0 else 0
        if first[1] == 0 and length > 2 and nums[first[1]] > nums[first[1]+1]:
            rotate = 1
        
        if length < 4 and first[1] == 0:
            try:
                ans = nums.index(target)
                return ans
            except:
                pass
        nums = nums[rotate:length] + nums[:rotate]
        first = 0
        end = length-1
        while first <= end:
            
            mid = (first + end) // 2 
            if nums[mid] == target:
                return (mid + rotate) % length
            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    first = mid + 1
            
        return -1