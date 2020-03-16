class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        if len(nums) < 3: return False
        
        minNum = [nums[0], float('inf')]
        
        for i in range(1, len(nums)):
            if nums[i] <= minNum[0]:
                minNum[0] = nums[i]
            elif nums[i] < minNum[1]:
                minNum[1] = nums[i]
            elif nums[i] > minNum[1]:
                return True
        return False