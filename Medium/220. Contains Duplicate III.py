class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool: 
        for i in range(max(1,len(nums))):
            for j in range(i+1,min(i+k+1,len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True
                
        return False