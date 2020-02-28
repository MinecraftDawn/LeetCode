class Solution:
    def countRangeSum(self, nums: list, lower: int, upper: int) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if lower <= sum(nums[i:j]) <= upper:
                    ans.append([i,j])
                    
        return len(ans)