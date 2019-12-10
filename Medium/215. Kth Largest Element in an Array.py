class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
       nums.sort(reverse=True)
       return nums[k-1]