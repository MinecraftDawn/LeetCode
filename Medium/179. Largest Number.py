from functools import cmp_to_key
def customSort(a, b):
    if a+b >= b+a: return -1
    else: return 1
    
class Solution:
    def largestNumber(self, nums: list) -> str:
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(customSort))
        if nums[0] == "0" or not nums: return "0"
        return "".join(nums)