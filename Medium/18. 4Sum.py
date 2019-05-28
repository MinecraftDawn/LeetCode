class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        if len(nums) < 4: return []
        nums.sort()
        length = len(nums)
        answers = []
        
        for j in range(length-3):
            num0 = nums[j]
            for i in range(j+1,length-2):
                num1 = nums[i]
                left = i + 1
                right = length - 1
                
                while left < right:
                    num2 = nums[left]
                    num3 = nums[right]
    
                    if num0 + num1 + num2 + num3 == target:
                        ans = [num0,num1,num2,num3]
                        answers.append(tuple(ans))
                        
                        right -= 1
                        left += 1
                    elif num0 + num1 + num2 + num3 > target:
                        right -= 1
                    else:
                        left += 1
            answers = list(set(answers))
            answers2 = []
            for i in answers:
                answers2.append(list(i))
        return answers2