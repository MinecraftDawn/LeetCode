#Reference: https://leetcode.com/problems/patching-array/discuss/338621/Python-O(n)-with-detailed-explanation
class Solution:
    def minPatches(self, nums: list, n: int) -> int:
        covered = 0
        ans = 0
        for num in nums:
            while num > covered + 1:
                ans += 1
                covered = covered * 2 + 1
                if covered >= n:
                    return ans
            
            covered += num
            if covered >= n:
                return ans
            
        while covered < n:
            ans += 1
            covered = covered * 2 + 1
            
        return ans