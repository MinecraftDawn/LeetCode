class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        numsMap = {num:index for index,num in enumerate(nums)}
        
        for index,num in enumerate(nums):
            if target-num in numsMap and numsMap[target-num] != index:
                return [index, numsMap[target-num]]