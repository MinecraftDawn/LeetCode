class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) <= 2: return len(nums)
        
        preNum = nums[0]
        times = 1
        ans = 1
        i = 1
        while i < len(nums):
            if nums[i] == preNum:
                times += 1
                if times > 2:
                    del nums[i]
                    i -= 1
                else:
                    ans += 1
            else:
                preNum = nums[i]
                ans += 1
                times = 1
            i += 1
        return ans