import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool: 
        kList = []
        for i in range(len(nums)):
            if len(kList) > k:
                kList.pop(bisect.bisect_left(kList, nums[i-k-1]))
            if bisect.bisect_right(kList, nums[i]+t) - bisect.bisect_left(kList, nums[i]-t) >= 1:
                return True
            
            bisect.insort_left(kList, nums[i])
        return False