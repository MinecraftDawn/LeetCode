class Solution:
    def canJump(self, nums: list) -> bool:
        if len(nums) == 1: return True
        
        index = 0
        curStep = 0
        while index < len(nums):
            curStep = max(curStep,nums[index])
            if curStep == 0: break
            curStep -= 1
            index += 1
        
        print(index)
        if index >= len(nums)-1:
            return True
        else:
            return False