class Solution:
    def countSmaller(self, nums: list) -> list:
        ans = [0] * len(nums)
        for i,num in enumerate(nums):
            for j in range(i):
                if nums[j] > num:
                    ans[j] += 1