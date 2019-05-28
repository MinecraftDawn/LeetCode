class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        length = len(nums)
        close = nums[0] + nums[1] + nums[2]
        
        for i in range(length-2):
            num1 = nums[i]
            left = i+1
            right = length - 1
            
            while left < right:
                num2 = nums[left]
                num3 = nums[right]
                
                if num1 + num2 + num3 == target:
                    return target
                elif num1 + num2 + num3 < target:
                    left += 1
                else:
                    right -= 1
                if abs(num1 + num2 + num3 - target) < abs(close - target):
                        close = num1 + num2 + num3
        return close