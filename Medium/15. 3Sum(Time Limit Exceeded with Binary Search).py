class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        length = len(nums)
        answers = []
        
        for i in range(length-2):
            for j in range(i+1, length-1):
                thirdNum = -(nums[i] + nums[j])
                left = j+1
                right = length - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == thirdNum:
                        ans = [nums[i],nums[j],nums[mid]]
                        ans.sort()
                        if ans not in answers:
                            answers.append(ans)
                        break
                    elif nums[mid] > thirdNum:
                        right = mid - 1
                    else:
                        left = mid + 1
                
        return answers