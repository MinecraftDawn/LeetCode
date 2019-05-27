class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        length = len(nums)
        answers = []
        
        for i in range(length-2):
            num1 = nums[i]
            left = i + 1
            right = length - 1
            
            while left < right:
                num2 = nums[left]
                num3 = nums[right]

                if num1 + num2 + num3 == 0:
                    ans = [num1,num2,num3]
                    answers.append(tuple(ans))
                    
                    right -= 1
                    left += 1
                elif num1 + num2 + num3 > 0:
                    right -= 1
                else:
                    left += 1
        answers = list(set(answers))
        answers2 = []
        for i in answers:
            answers2.append(list(i))
        return answers2