class Solution:
    def countRangeSum(self, nums: list, lower: int, upper: int) -> int:
        dp = [0]
        total = 0
        for num in nums:
            total += num
            dp.append(total)
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if lower <= dp[j]-dp[i] <= upper:
                    ans += 1          

        return ans