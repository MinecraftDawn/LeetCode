class Solution:
    def splitArray(self, nums: list, m: int) -> int:
        if m <= 1: return sum(nums)

        ans = float("inf")
        for i in range(1,len(nums)):
            ans = min(ans, max(sum(nums[:i]), self.splitArray(nums[i:],m-1)))

        return ans