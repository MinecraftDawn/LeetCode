class Solution:
    def findMin(self, nums: list) -> int:
        ans = nums[0]
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                ans = nums[mid+1]
                
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid
        return ans