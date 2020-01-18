class Solution:
    def firstBadVersion(self, n:int) -> int:
        if isBadVersion(1): return 1
        
        left,right = 1,n
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            bad_good = isBadVersion(mid)
            
            if bad_good: right = mid
            else: left = mid
                
        return right