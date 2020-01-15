class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        total = (length+1) * length // 2
        return total - sum(nums)