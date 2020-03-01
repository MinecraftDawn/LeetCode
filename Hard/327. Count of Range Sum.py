# Reference: https://leetcode.com/problems/count-of-range-sum/discuss/524747/Python-140ms-solution-by-using-bisect-short-code
import bisect
class Solution:
    def countRangeSum(self, nums: list, lower: int, upper: int) -> int:
        dp = []
        total = 0
        for num in nums:
            total += num
            dp.append(total)
            
        print(dp)
        
        ans = 0
        cur = [0]
        for val in dp:
            right = bisect.bisect_right(cur, val - lower)
            left = bisect.bisect_left(cur, val - upper)
            ans += right - left
            bisect.insort(cur, val)    

        return ans